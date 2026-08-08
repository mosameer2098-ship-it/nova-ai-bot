import logging
import os

from aiohttp import web

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
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
# HEALTH CHECK SERVER
# ==========================================

async def health(request):
    return web.Response(
        text="Nova AI Bot is running!"
    )


async def start_web_server():
    port = int(os.environ.get("PORT", 10000))

    app = web.Application()

    app.router.add_get("/", health)
    app.router.add_get("/health", health)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(
        runner,
        "0.0.0.0",
        port,
    )

    await site.start()

    logger.info(
        f"🌐 Health server running on port {port}"
    )


# ==========================================
# MAIN
# ==========================================

async def main():

    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN environment variable is missing."
        )

    # Telegram application
    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    # Commands
    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CommandHandler("help", help_command)
    )

    application.add_handler(
        CommandHandler("clear", clear_command)
    )

    # Normal messages
    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler,
        )
    )

    # Start Telegram bot
    await application.initialize()
    await application.start()
    await application.updater.start_polling(
        drop_pending_updates=True
    )

    logger.info(
        "🤖 Nova AI Bot started successfully!"
    )

    # Start Render HTTP server
    await start_web_server()

    # Keep application alive
    await __import__("asyncio").Event().wait()


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
