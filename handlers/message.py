from telegram import Update
from telegram.ext import ContextTypes
from utils.ai import generate_reply


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    await update.message.chat.send_action("typing")

    ai_reply = generate_reply(user_message)

    await update.message.reply_text(ai_reply)
