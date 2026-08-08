import os
import httpx

from utils.memory import get_chat, update_chat

HF_TOKEN = os.getenv("HF_TOKEN")

MODEL = "HuggingFaceH4/zephyr-7b-beta"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"


async def generate_reply(user_id, message):
    history = get_chat(user_id)

    prompt = """You are NOVA, a friendly AI Telegram assistant.
Reply naturally and helpfully.
If the user speaks Hindi or Hinglish, reply in Hindi/Hinglish.

Conversation:
"""

    for chat in history:
        prompt += f"User: {chat['user']}\n"
        prompt += f"NOVA: {chat['bot']}\n"

    prompt += f"User: {message}\nNOVA:"

    try:
        headers = {
            "Authorization": f"Bearer {HF_TOKEN}",
            "Content-Type": "application/json",
        }

        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 300,
                "temperature": 0.7,
                "return_full_text": False,
            },
        }

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                API_URL,
                headers=headers,
                json=payload,
            )

        if response.status_code != 200:
            print("HUGGING FACE ERROR:", response.status_code, response.text)
            return "⚠️ Nova AI abhi response nahi de pa raha. Thodi der baad try karo."

        data = response.json()

        if isinstance(data, list) and data:
            reply = data[0].get("generated_text", "").strip()
        else:
            reply = ""

        if not reply:
            return "⚠️ AI se response nahi mila."

        update_chat(user_id, message, reply)
        return reply

    except Exception as e:
        print("HUGGING FACE ERROR:", type(e).__name__, e)
        return "⚠️ Nova AI abhi response nahi de pa raha. Thodi der baad try karo."
