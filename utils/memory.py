import json
import os


DATA_FILE = "data/chats.json"


def _load_data():
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


def _save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2
        )


def get_chat(user_id):
    data = _load_data()

    return data.get(str(user_id), [])


def update_chat(user_id, user_message, bot_reply):
    data = _load_data()

    user_id = str(user_id)

    if user_id not in data:
        data[user_id] = []

    data[user_id].append({
        "user": user_message,
        "bot": bot_reply
    })

    # Keep only the latest 20 conversations
    data[user_id] = data[user_id][-20:]

    _save_data(data)


def clear_chat(user_id):
    data = _load_data()

    user_id = str(user_id)

    if user_id in data:
        del data[user_id]

    _save_data(data)
