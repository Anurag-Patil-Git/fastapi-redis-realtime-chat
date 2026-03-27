from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import redis
import asyncio
import json
import sqlite3
from database import save_message, get_messages

app = FastAPI()

# Serve frontend
@app.get("/")
async def get():
    with open("index.html") as f:
        return HTMLResponse(f.read())

# Redis
redis_client = redis.Redis(host="localhost",port=6379,decode_responses=True)

# Store clients per room
rooms = {}

# Redis listener
async def redis_listener():
    pubsub = redis_client.pubsub()
    pubsub.subscribe("chat")

    while True:
        message = pubsub.get_message()

        if message and message["type"] == "message":
            data = json.loads(message["data"])
            room = data["room"]

            if room in rooms:
                for client in rooms[room]:
                    await client.send_text(json.dumps(data))

        await asyncio.sleep(0.01)

@app.on_event("startup")
async def startup():
    asyncio.create_task(redis_listener())

# Clear DB + rooms
@app.get("/clear")
def clear_db():
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM messages")
    conn.commit()
    conn.close()

    # Clear global rooms in Redis
    redis_client.delete("chat_rooms")

    return {"message": "Database cleared successfully"}

@app.get("/rooms")
def get_rooms():
    rooms=list(redis_client.smembers("chat_rooms"))
    return {"rooms": rooms}

# Get total rooms
@app.get("/rooms/count")
def get_room_count():
    count = redis_client.scard("chat_rooms")
    return {"count": count}

# WebSocket
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    username = await websocket.receive_text()
    room = await websocket.receive_text()

    # Add room to global Redis set
    redis_client.sadd("chat_rooms", room)

    # Add client to local room
    if room not in rooms:
        rooms[room] = []

    rooms[room].append(websocket)

    # Send old messages
    old_messages = get_messages(room)
    for user, msg in old_messages:
        await websocket.send_text(json.dumps({
            "username": user,
            "message": msg
        }))

    try:
        while True:
            data = await websocket.receive_text()

            message_data = {
                "username": username,
                "room": room,
                "message": data
            }

            # Save to DB
            save_message(username, room, data)

            # Publish to Redis
            redis_client.publish("chat", json.dumps(message_data))

    except Exception as e:
        print("Disconnected:", e)

        if room in rooms and websocket in rooms[room]:
            rooms[room].remove(websocket)