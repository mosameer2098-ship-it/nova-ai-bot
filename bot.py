import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN
from utils.ai import generate_reply


# -----------------------------
# Logging
# -----------------------------

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# -----------------------------
# /start
# -----------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello!\n\n"
        "Main Nova AI hoon 🤖\n"
        "Mujhse Hindi, Hinglish ya English mein baat kar sakte ho.\n\n"
        "Bas message bhejo aur conversation start karo."
    )


# -----------------------------
# /help
# -----------------------------

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Nova AI Help\n\n"
        "/start - Bot start karein\n"
        "/help - Help menu\n"
        "/clear - Chat history clear karein\n\n"
        "Normal message bhejkar mujhse baat karein."
    )


# -----------------------------
# /clear
# -----------------------------

async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧹 Chat history clear karne ka system next step mein connect hoga."
    )


# -----------------------------
# Normal Messages
# -----------------------------

async def message_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    if not update.message or not update.message.text:
        return

    user_message = update.message.text

    try:
        # Typing indicator
        await update.message.chat.send_action("typing")

        # Generate AI response
        reply = generate_reply(user_message)

        # Telegram message limit handling
        if len(reply) <= 4000:
            await update.message.reply_text(reply)
        else:
            for i in range(0, len(reply), 4000):
                await update.message.reply_text(reply[i:i + 4000])

    except Exception:
        logger.exception("AI response error")

        await update.message.reply_text(
            "⚠️ Sorry, abhi AI response dene mein problem aa rahi hai. "
            "Please thodi der baad dobara try karo."
        )


# -----------------------------
# Error Handler
# -----------------------------

async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE
):
    logger.error(
        "Exception while handling update:",
        exc_info=context.error,
    )


# -----------------------------
# Main
# -----------------------------

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("clear", clear_command))

    # Normal text messages
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler
        )
    )

    # Error handling
    app.add_error_handler(error_handler)

    logger.info("🤖 Nova AI Bot is starting...")

    # Start bot
    app.run_polling(
        drop_pending_updates=True
    )


if __name__ == "__main__":
    main()
