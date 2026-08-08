import os
from huggingface_hub import InferenceClient

from utils.memory import get_chat, update_chat


HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN environment variable is missing.")

client = InferenceClient(
    provider="hf-inference",
    api_key=HF_TOKEN
)


async def generate_reply(user_id, message):
    history = get_chat(user_id)

    system_prompt = """
You are NOVA, a friendly and intelligent Telegram AI assistant.

Rules:
- Reply naturally and helpfully.
- If the user speaks Hindi or Hinglish, reply in Hindi/Hinglish.
- If the user speaks English, reply in English.
- Keep replies clear and easy to understand.
- Do not mention that you are using Hugging Face.
- Do not make up information.
- Answer the user's actual question directly.
"""

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    # Previous conversation memory
    for chat in history:
        messages.append({
            "role": "user",
            "content": str(chat["user"])
        })

        messages.append({
            "role": "assistant",
            "content": str(chat["bot"])
        })

    # Current message
    messages.append({
        "role": "user",
        "content": message
    })

    try:
        response = client.chat_completion(
            messages=messages,
            model="Qwen/Qwen2.5-7B-Instruct",
            max_tokens=500,
            temperature=0.7
        )

        reply = response.choices[0].message.content

        if not reply:
            reply = "⚠️ Abhi response nahi mila. Dobara try karo."

        # Save conversation
        update_chat(user_id, message, reply)

        return reply.strip()

    except Exception as e:
        print("=" * 60)
        print("HUGGING FACE ERROR")
        print("TYPE:", type(e).__name__)
        print("MESSAGE:", str(e))
        print("=" * 60)

        return (
            "⚠️ Nova AI abhi response nahi de pa raha.\n\n"
            "Thodi der baad dobara try karo."
    )
