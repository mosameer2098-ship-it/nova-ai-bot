from telegram import Update
from telegram.ext import ContextTypes

from utils.ai import generate_reply


async def message_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    # Message check
    if not update.message or not update.message.text:
        return

    # User information
    user_id = update.effective_user.id if update.effective_user else 0
    message = update.message.text

    # Typing indicator
    await update.message.chat.send_action("typing")

    # AI/reply system se relevant reply lo
    reply = await generate_reply(
        user_id=user_id,
        message=message
    )

    # Reply send karo
    await update.message.reply_text(
        f"🤖 𝗡𝗢𝗩𝗔: {reply}"
    )
