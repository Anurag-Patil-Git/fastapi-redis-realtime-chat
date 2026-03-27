import sqlite3

conn = sqlite3.connect("chat.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    room TEXT,
    message TEXT
)
""")

conn.commit()


def save_message(username, room, message):
    cursor.execute(
        "INSERT INTO messages (username, room, message) VALUES (?, ?, ?)",
        (username, room, message),
    )
    conn.commit()


def get_messages(room):
    cursor.execute(
        "SELECT username, message FROM messages WHERE room=?",
        (room,),
    )
    return cursor.fetchall()