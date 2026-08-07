from telegram import Update
from telegram.ext import ContextTypes

from utils.memory import clear_chat


async def clear_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    user_id = update.effective_user.id

    clear_chat(user_id)

    await update.message.reply_text(
        "🧹 Chat history clear kar di gayi hai.\n\n"
        "Ab hum fresh conversation se start karenge. 😊"
    )
