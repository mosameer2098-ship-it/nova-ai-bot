from google import genai
from config import GEMINI_API_KEY
from utils.memory import get_chat, update_chat

client = genai.Client(api_key=GEMINI_API_KEY)


async def generate_reply(user_id, message):
    history = get_chat(user_id)

    prompt = """You are NOVA, a friendly AI Telegram assistant.
Reply naturally and helpfully.
If the user speaks Hindi or Hinglish, reply in Hindi/Hinglish.

"""

    for chat in history:
        prompt += f"User: {chat['user']}\n"
        prompt += f"NOVA: {chat['bot']}\n"

    prompt += f"User: {message}\nNOVA:"

    try:
        response = await client.aio.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        reply = response.text or "⚠️ AI se response nahi mila."

        update_chat(user_id, message, reply)

        return reply

    except Exception as e:
        print(f"GEMINI ERROR: {type(e).__name__}: {e}")

        return (
            "⚠️ Nova AI abhi response nahi de pa raha.\n"
            "Thodi der baad dobara try karo."
        )
