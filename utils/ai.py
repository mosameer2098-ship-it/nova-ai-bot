# utils/ai.py

import random
import re

# ============================================================
# ALL REPLY FILES
# ============================================================

from utils.replies import REPLIES

# Ye files agar tumhare project me hain to import hongi.
# Kisi file ka naam alag hai to us file ko yahan add kar denge.

try:
    from utils.romantic_chat import ROMANTIC_CHAT
except ImportError:
    ROMANTIC_CHAT = {}

try:
    from utils.flirty_chat import FLIRTY_CHAT
except ImportError:
    FLIRTY_CHAT = {}

try:
    from utils.mixed_chat import MIXED_CHAT
except ImportError:
    MIXED_CHAT = {}

try:
    from utils.hot_chat import HOT_CHAT
except ImportError:
    HOT_CHAT = {}


# ============================================================
# COMBINE ALL REPLIES
# ============================================================

ALL_REPLIES = {}

ALL_REPLIES.update(REPLIES)
ALL_REPLIES.update(ROMANTIC_CHAT)
ALL_REPLIES.update(FLIRTY_CHAT)
ALL_REPLIES.update(MIXED_CHAT)
ALL_REPLIES.update(HOT_CHAT)


# ============================================================
# TEXT CLEANER
# ============================================================

def clean_text(text: str) -> str:
    """
    User ke message ko simple searchable text me convert karta hai.
    """

    if not text:
        return ""

    text = str(text).lower().strip()

    # Common symbols ko space me convert
    text = re.sub(r"[^\w\s]", " ", text)

    # Multiple spaces remove
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ============================================================
# WORD MATCHING
# ============================================================

def contains_keyword(text: str, keyword: str) -> bool:
    """
    Keyword ko smart way se match karta hai.

    Example:
    'hello dost' -> hello match hoga
    'good morning dost' -> good morning match hoga
    """

    text = clean_text(text)
    keyword = clean_text(keyword)

    if not text or not keyword:
        return False

    # Exact phrase
    if keyword in text:
        return True

    return False


# ============================================================
# FIND BEST MATCH
# ============================================================

def find_reply_key(message: str):
    """
    User ke message me sabse relevant keyword/category dhundta hai.

    Longer phrases ko priority milti hai.
    Example:

    'good morning dost'

    me 'good morning' ko 'morning' se pehle check karega.
    """

    text = clean_text(message)

    if not text:
        return None

    best_key = None
    best_score = 0

    for key in ALL_REPLIES.keys():

        key_clean = clean_text(key)

        if not key_clean:
            continue

        # Phrase/keyword match
        if key_clean in text:

            # Longer matching phrase ko higher priority
            score = len(key_clean)

            # Exact message ko extra priority
            if key_clean == text:
                score += 1000

            # Word count bhi priority deta hai
            score += len(key_clean.split()) * 100

            if score > best_score:
                best_score = score
                best_key = key

    return best_key


# ============================================================
# GET RANDOM REPLY
# ============================================================

def get_random_reply(key: str):
    """
    Matching category se random reply choose karta hai.
    """

    replies = ALL_REPLIES.get(key, [])

    if not replies:
        return None

    if isinstance(replies, str):
        return replies

    if not isinstance(replies, (list, tuple)):
        return None

    valid_replies = [
        str(reply).strip()
        for reply in replies
        if reply and str(reply).strip()
    ]

    if not valid_replies:
        return None

    return random.choice(valid_replies)


# ============================================================
# FALLBACK REPLIES
# ============================================================

FALLBACK_REPLIES = [

    "Hmm 😊 Ye interesting hai. Thoda aur batao.",

    "Achha 😄 Iske baare mein aur batao.",

    "Samajh raha hoon 🤖 Bolo, kya hua?",

    "Haan dost ❤️ Main sun raha hoon.",

    "Interesting 🤔 Thoda detail mein batao.",

    "Achha ji 😊 Phir kya hua?",

    "Bolo bhai 😎 Nova sun raha hai.",

    "Hmm 🤖 Iska thoda aur context do.",

    "Theek hai 😊 Tum apni baat continue karo.",

    "Main sun raha hoon ❤️ Batao.",

    "Achha 😊 Pura batao, main dhyan se sun raha hoon.",

    "Hmm 😄 Ye baat interesting lag rahi hai.",

    "Bolo dost 🤖 Main yahin hoon.",

    "Thoda aur explain karo 😊",

    "Samajhne ke liye thoda detail chahiye 😄",
]


# ============================================================
# MAIN REPLY FUNCTION
# ============================================================

async def generate_reply(user_id: int, message: str) -> str:
    """
    Main reply generator.

    Gemini/API ki zarurat nahi hai.
    Saari replies local files se aayengi.
    """

    # Empty message
    if not message or not message.strip():

        return "Kuch likho na 😊 Nova sun raha hai."


    # --------------------------------------------------------
    # Find best matching topic
    # --------------------------------------------------------

    key = find_reply_key(message)


    # --------------------------------------------------------
    # Matching reply mil gaya
    # --------------------------------------------------------

    if key:

        reply = get_random_reply(key)

        if reply:
            return reply


    # --------------------------------------------------------
    # Kuch match nahi mila
    # --------------------------------------------------------

    return random.choice(FALLBACK_REPLIES)


# ============================================================
# OPTIONAL SIMPLE FUNCTION
# ============================================================

def get_reply(message: str) -> str:
    """
    Synchronous version.
    Agar kisi aur file me async function use nahi karna
    ho to ye function use kiya ja sakta hai.
    """

    if not message or not message.strip():
        return "Kuch likho na 😊 Nova sun raha hai."

    key = find_reply_key(message)

    if key:

        reply = get_random_reply(key)

        if reply:
            return reply

    return random.choice(FALLBACK_REPLIES)
