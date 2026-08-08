import random
from telegram import Update
from telegram.ext import ContextTypes


REPLIES = [
    "Haan 😊 bolo, kya baat hai?",
    "Main yahin hoon 🤖 bolo kya help chahiye?",
    "Achha 😄 phir batao kya hua?",
    "Haan ji, sun raha hoon 👂",
    "Bilkul 👍 batao.",
    "Haha 😄 sahi hai!",
    "Samajh gaya 😊",
    "Thoda detail me batao, main help karta hoon.",
    "Koi tension nahi ❤️ main hoon na.",
    "Achha! Ye interesting hai 👀",
    "Haan bolo Sameer 😊",
    "Main tumhari baat sun raha hoon 🤖",
    "Bilkul, batao kya karna hai?",
    "Theek hai 👍 aage bolo.",
    "Hmm 🤔 samajh raha hoon.",
]


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message or not update.message.text:
        return

    await update.message.chat.send_action("typing")

    reply = random.choice(REPLIES)

    await update.message.reply_text(
        f"🤖 𝗡𝗢𝗩𝗔: {reply}"
    )
