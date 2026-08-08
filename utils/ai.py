# utils/ai.py

import random
import re

from utils.replies import REPLIES


def clean_text(text: str) -> str:
    """Message ko simple format me convert karta hai."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def find_reply_key(message: str):
    """User ke message me matching keyword/category dhundta hai."""

    text = clean_text(message)

    # Exact / phrase matching
    priority_keys = sorted(REPLIES.keys(), key=len, reverse=True)

    for key in priority_keys:
        key_clean = clean_text(key)

        if key_clean in text:
            return key

    return None


async def generate_reply(user_id: int, message: str) -> str:
    """
    Gemini/API ke bina fixed replies se response deta hai.
    """

    if not message or not message.strip():
        return "Kuch likho na 😊 Nova sun raha hai."

    key = find_reply_key(message)

    if key:
        replies = REPLIES.get(key, [])

        if replies:
            return random.choice(replies)

    # Unknown message ke liye fallback replies
    fallback_replies = [
        "Hmm 😊 Ye interesting hai. Thoda aur batao.",
        "Achha 😄 Iske baare me aur batao.",
        "Samajh raha hoon 🤖 Bolo, kya hua?",
        "Haan dost ❤️ Main sun raha hoon.",
        "Interesting 🤔 Thoda detail me batao.",
        "Achha ji 😊 Phir kya hua?",
        "Bolo bhai 😎 Nova sun raha hai.",
        "Hmm 🤖 Iska thoda aur context do.",
        "Theek hai 😊 Tum apni baat continue karo.",
        "Main sun raha hoon ❤️ Batao."
    ]

    return random.choice(fallback_replies)
