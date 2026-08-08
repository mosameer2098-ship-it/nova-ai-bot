from telegram import Update
from telegram.ext import ContextTypes
from utils.ai import generate_reply


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id
    message = update.message.text

    await update.message.chat.send_action("typing")

    reply = await generate_reply(user_id, message)

    await update.message.reply_text(reply)
