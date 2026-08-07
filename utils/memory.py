import json
import os

MEMORY_FILE = "data/chats.json"

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump({}, f)


def load_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


def get_chat(user_id):
    data = load_memory()
    return data.get(str(user_id), [])


def update_chat(user_id, user_msg, bot_msg):
    data = load_memory()

    history = data.get(str(user_id), [])

    history.append({
        "user": user_msg,
        "bot": bot_msg
    })

    history = history[-10:]  # Sirf last 10 messages

    data[str(user_id)] = history

    save_memory(data)
