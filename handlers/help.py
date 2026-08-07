from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Nova AI Help\n\n"
        "💬 Mujhse normal conversation kar sakte ho.\n"
        "🇮🇳 Hindi aur Hinglish supported hai.\n"
        "🇬🇧 English bhi supported hai.\n\n"
        "📌 Commands:\n"
        "/start - Bot start karein\n"
        "/help - Help menu\n"
        "/clear - Chat history clear karein\n\n"
        "💡 Example:\n"
        "Mujhe ek funny joke sunao 😄"
    )
