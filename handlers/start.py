from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    name = user.first_name if user.first_name else "Friend"

    await update.message.reply_text(
        f"👋 Hello {name}!\n\n"
        "🤖 Main Nova AI hoon.\n"
        "Tum mujhse Hindi, Hinglish ya English mein baat kar sakte ho.\n\n"
        "💬 Bas message bhejo aur conversation start karo.\n\n"
        "Commands:\n"
        "/start - Bot start karein\n"
        "/help - Help menu\n"
        "/clear - Chat history clear karein"
    )
