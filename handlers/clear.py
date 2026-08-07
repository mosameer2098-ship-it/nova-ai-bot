import json
from telegram import Update
from telegram.ext import ContextTypes

MEMORY_FILE = "data/chats.json"

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)

        if user_id in data:
            del data[user_id]

        with open(MEMORY_FILE, "w") as f:
            json.dump(data, f, indent=4)

        await update.message.reply_text("✅ Chat history cleared.")

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")
