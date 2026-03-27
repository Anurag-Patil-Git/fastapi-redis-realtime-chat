# 🚀 fastapi-redis-realtime-chat

A scalable **real-time chat system** built using modern backend technologies, enabling instant communication with **multi-room support, persistent storage, and distributed messaging**.

---

## ⚡ Key Highlights

- 💬 Real-time messaging using WebSockets  
- 🏠 Multi-room chat architecture  
- ⚡ Redis Pub/Sub for scalable message broadcasting  
- 💾 Persistent chat history with SQLite  
- 👥 Live user & room tracking  
- 🧹 Clear chat functionality  
- 🎨 Clean and responsive UI  

---

## 🧠 Architecture Overview
```
Client (Browser)
│
▼
FastAPI (WebSocket Server)
│
├── Redis Pub/Sub → Real-time message distribution
└── SQLite DB → Persistent message storage
```
---

## 🛠️ Tech Stack

- **Backend Framework:** FastAPI  
- **Realtime Communication:** WebSockets  
- **Message Broker:** Redis (Pub/Sub)  
- **Database:** SQLite  
- **Frontend:** HTML, CSS, JavaScript  
- **Concurrency:** AsyncIO  

---

## 📂 Core Components

- `main.py` → FastAPI app, WebSocket handling, Redis integration  
- `database.py` → Message storage & retrieval logic  
- `index.html` → Frontend UI & client-side WebSocket handling  

---

## 🔥 Key Features Breakdown

### 🔌 WebSocket Layer
- Maintains persistent connections  
- Enables bidirectional real-time communication  

### ⚡ Redis Integration
- Publishes messages to a central channel  
- Ensures scalability across multiple clients/instances  

### 💾 Database Layer
- Stores chat messages by room  
- Loads chat history on user join  

---

## 📡 API Endpoints

| Endpoint        | Method | Description              |
|----------------|--------|--------------------------|
| `/`            | GET    | Serve frontend           |
| `/ws`          | WS     | WebSocket connection     |
| `/rooms`       | GET    | List active rooms        |
| `/rooms/count` | GET    | Total room count         |
| `/clear`       | GET    | Clear chat history       |

---

## 🚀 Getting Started

```bash
# Install dependencies
pip install fastapi uvicorn redis

# Start Redis server
redis-server

# Run application
uvicorn main:app --reload
Open → http://localhost:8000
```
---
## 👨‍💻 Author

**Anurag Patil**

🔗 GitHub  
https://github.com/Anurag-Patil-Git  

🔗 LinkedIn  
https://www.linkedin.com/in/anurag-patil/

---

⭐ If you like this project, consider giving it a star!
