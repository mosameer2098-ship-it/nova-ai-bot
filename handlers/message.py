from telegram import Update
from telegram.ext import ContextTypes

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    await update.message.reply_text(
        f"Received: {user_message}"
    )
