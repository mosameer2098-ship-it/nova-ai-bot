import google.generativeai as genai
from config import GEMINI_API_KEY
from utils.memory import get_chat, update_chat

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_reply(user_id, message):
    history = get_chat(user_id)

    prompt = ""

    for chat in history:
        prompt += f"User: {chat['user']}\n"
        prompt += f"Bot: {chat['bot']}\n"

    prompt += f"User: {message}\nBot:"

    response = model.generate_content(prompt)

    reply = response.text

    update_chat(user_id, message, reply)

    return reply
