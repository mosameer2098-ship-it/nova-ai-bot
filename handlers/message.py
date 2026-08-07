from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from utils.ai import generate_reply


async def message_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    if not update.message or not update.message.text:
        return

    user_id = update.effective_user.id
    user_message = update.message.text.strip()

    if not user_message:
        return

    try:
        # Show typing indicator
        await update.message.chat.send_action(
            action=ChatAction.TYPING
        )

        # Generate AI response
        reply = generate_reply(
            user_id,
            user_message
        )

        # Telegram message limit
        max_length = 4000

        if len(reply) <= max_length:
            await update.message.reply_text(reply)
        else:
            for start in range(0, len(reply), max_length):
                await update.message.reply_text(
                    reply[start:start + max_length]
                )

    except Exception:
        await update.message.reply_text(
            "⚠️ Sorry, abhi mujhe response dene mein problem aa rahi hai. "
            "Thodi der baad dobara try karo."
        )
