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
from handlers.start import start
from handlers.help import help_command
from handlers.clear import clear_command
from handlers.message import message_handler


# ==========================================
# LOGGING
# ==========================================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# ==========================================
# ERROR HANDLER
# ==========================================

async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE,
):
    logger.error(
        "Exception while handling update:",
        exc_info=context.error,
    )


# ==========================================
# MAIN BOT
# ==========================================

def main():

    # Check Telegram Bot Token
    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN environment variable is missing."
        )

    # Create Telegram application
    app = Application.builder().token(BOT_TOKEN).build()

    # ======================================
    # COMMANDS
    # ======================================

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("help", help_command)
    )

    app.add_handler(
        CommandHandler("clear", clear_command)
    )

    # ======================================
    # NORMAL TEXT MESSAGES
    # ======================================

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler,
        )
    )

    # ======================================
    # ERROR HANDLER
    # ======================================

    app.add_error_handler(error_handler)

    # ======================================
    # START BOT
    # ======================================

    logger.info("🤖 Nova AI Bot is starting...")

    app.run_polling(
        drop_pending_updates=True
    )


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":
    main()
