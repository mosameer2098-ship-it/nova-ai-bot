from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from handlers.start import start
from handlers.help import help_command
from handlers.message import message_handler

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
)

print("🤖 Telegram AI Bot Started...")

app.run_polling()
from handlers.clear import clear
app.add_handler(CommandHandler("clear", clear))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("clear", clear))
