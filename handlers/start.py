from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! Main AI Telegram Bot hoon.\n\nMujhe koi bhi message bhejo."
    )
