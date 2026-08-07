import json
import os

MEMORY_FILE = "data/chats.json"
MAX_MESSAGES = 10


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


def save_memory(data):
    os.makedirs("data", exist_ok=True)

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def get_chat(user_id):
    data = load_memory()
    return data.get(str(user_id), [])


def add_message(user_id, user_message, bot_message):
    data = load_memory()

    user_id = str(user_id)

    history = data.get(user_id, [])

    history.append({
        "user": user_message,
        "bot": bot_message
    })

    # Sirf last 10 conversation pairs rakho
    data[user_id] = history[-MAX_MESSAGES:]

    save_memory(data)


def clear_chat(user_id):
    data = load_memory()

    user_id = str(user_id)

    if user_id in data:
        del data[user_id]
        save_memory(data)

    return True
