from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Bot Start\n"
        "/help - Help Menu\n"
        "/clear - Chat History Clear (baad me add karenge)"
    )
