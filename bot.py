import logging

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from handlers.start import start
from handlers.help import help_command
from handlers.clear import clear
from handlers.message import message_handler
from error_handler import error_handler

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

# Create Application
app = Application.builder().token(BOT_TOKEN).build()

# Commands
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("clear", clear))

# Message Handler
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
)

# Error Handler
app.add_error_handler(error_handler)

print("🤖 Telegram AI Bot Started Successfully...")

# Run Bot
app.run_polling(
    allowed_updates=["message"]
)
