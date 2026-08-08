import random

# ============================================================
# NOVA OFFLINE CHAT SYSTEM
# No Gemini
# No Hugging Face
# No API
# ============================================================

CHAT_REPLIES = {

    # ---------------- GREETINGS ----------------

    "hi": [
        "Hi 👋 Kaise ho?",
        "Hello 😊 Kya haal hai?",
        "Hey 😎 NOVA yahan hai!",
        "Hi bhai ❤️ Kya chal raha hai?",
        "Hello! 🤖 Batao kya baat hai?"
    ],

    "hello": [
        "Hello 👋 Kaise ho?",
        "Hey! 😊 NOVA ready hai.",
        "Hello bhai ❤️",
        "Hi 😎 Kya haal hai?",
        "Hello! Batao kya karna hai 🤖"
    ],

    "hey": [
        "Hey 😎 Kya scene hai?",
        "Hey! 👋 Kaise ho?",
        "Haan bhai bolo 😄",
        "NOVA sun raha hai 🤖",
        "Hey there! ❤️"
    ],

    "hii": [
        "Hiii 😄❤️",
        "Hello hello 👋",
        "Haan bhai 😎",
        "Hiii! NOVA present 🤖",
        "Kaise ho? 😊"
    ],

    "hlo": [
        "Hello 👋",
        "Haan bolo 😄",
        "Hlo bhai ❤️",
        "NOVA online hai 🤖",
        "Kya haal hai? 😎"
    ],

    # ---------------- HOW ARE YOU ----------------

    "kaise ho": [
        "Main bilkul theek hoon 😄 Tum kaise ho?",
        "NOVA ekdum mast hai 🤖 Tum batao?",
        "Main badhiya hoon ❤️ Tumhara din kaisa ja raha hai?",
        "Bilkul fit 😎 Tum sunao?",
        "Main mast hoon 😄"
    ],

    "kya haal hai": [
        "Mast haal hai 😎 Tumhara kya haal hai?",
        "Sab badhiya 🤖 Tum batao?",
        "Ekdam first class 😄",
        "NOVA ka haal hamesha mast ❤️",
        "Badhiya bhai 😎"
    ],

    "theek ho": [
        "Haan bilkul theek hoon 😊",
        "Ekdam fit 🤖",
        "Haan bhai, mast hoon 😎",
        "100% theek ❤️",
        "NOVA hamesha ready 😄"
    ],

    "mai theek": [
        "Ye sunkar achha laga 😊",
        "Wah! Aise hi khush raho ❤️",
        "Great 😎",
        "Bahut badhiya bhai 🤖",
        "Nice! 😄"
    ],

    # ---------------- NAME ----------------

    "naam kya": [
        "Mera naam NOVA hai 🤖",
        "Main NOVA hoon 😎",
        "Mujhe NOVA ke naam se bula sakte ho ❤️",
        "NOVA naam hai mera 🤖",
        "Main tumhara NOVA assistant hoon 😄"
    ],

    "tumhara naam": [
        "Mera naam NOVA hai 🤖",
        "NOVA 😎",
        "Main NOVA hoon ❤️",
        "Tum mujhe NOVA bula sakte ho.",
        "NOVA reporting! 🤖🔥"
    ],

    "who are you": [
        "Main NOVA hoon 🤖 Tumhara friendly assistant.",
        "I'm NOVA 😎",
        "NOVA naam hai mera ❤️",
        "Main tumse chat karne wala assistant hoon 🤖"
    ],

    # ---------------- WHAT ARE YOU DOING ----------------

    "kya kar rahe": [
        "Bas tumse baat kar raha hoon 😄",
        "Tumhare message ka wait kar raha tha 🤖",
        "Abhi tumse chatting kar raha hoon 😎",
        "NOVA full active hai 🔥",
        "Bas online hoon bhai ❤️"
    ],

    "kaha ho": [
        "Main yahin hoon 🤖",
        "Tumhare Telegram me 😎",
        "NOVA kahin nahi gaya 😂",
        "Yahin tumhare saath chat kar raha hoon ❤️",
        "Online hoon bhai 👋"
    ],

    "busy ho": [
        "Nahi bhai, tumhare liye free hoon 😄",
        "NOVA kabhi busy nahi 😎",
        "Nahi, bolo kya hua? 🤖",
        "Bilkul free ❤️"
    ],

    # ---------------- THANKS ----------------

    "thank you": [
        "You're welcome! 😊❤️",
        "Koi baat nahi 😄",
        "Always welcome 🤖",
        "Arey isme thank you ki kya baat hai 😎",
        "Khushi hui help karke ❤️"
    ],

    "thanks": [
        "You're welcome 😊",
        "Koi baat nahi bhai ❤️",
        "Anytime! 🤖",
        "Mention not 😄",
        "Welcome welcome 😎"
    ],

    "shukriya": [
        "Aapka swagat hai 😊",
        "Koi baat nahi ❤️",
        "Hamesha bhai 🤖",
        "Khushi hui 😄",
        "Welcome 😎"
    ],

    # ---------------- MORNING ----------------

    "good morning": [
        "Good Morning 🌅☀️ Aaj ka din shandar ho!",
        "Good Morning 😊☕",
        "Suprabhat! 🌞",
        "Morning bhai 😎",
        "Good Morning ❤️ Aaj kya plan hai?"
    ],

    "morning": [
        "Good Morning 🌅",
        "Morning bhai 😄",
        "Suprabhat ❤️",
        "Good morning! ☀️",
        "Aaj ka din mast ho 🤖"
    ],

    # ---------------- NIGHT ----------------

    "good night": [
        "Good Night 🌙😴 Sweet dreams!",
        "Shubh Ratri 🌙❤️",
        "Good night! Kal phir baat karenge 😄",
        "Achhi neend lena 😴",
        "Good night bhai 🤖❤️"
    ],

    "goodnight": [
        "Good Night 🌙",
        "Sweet dreams 😴❤️",
        "Shubh Ratri 😊",
        "Kal milte hain 🤖",
        "Good night 😎"
    ],

    # ---------------- BYE ----------------

    "bye": [
        "Bye! 👋 Phir milte hain.",
        "Okay bye 😊 Apna khayal rakhna.",
        "See you soon 🤖❤️",
        "Bye bhai 😎",
        "Phir baat karenge 👋"
    ],

    "tata": [
        "Tata 👋😂",
        "Bye bye ❤️",
        "Okay tata 😄",
        "Phir milenge 🤖",
        "Tata bhai 😎"
    ],

    # ---------------- LOVE ----------------

    "love you": [
        "Aww ❤️😊",
        "NOVA ki taraf se unlimited ❤️",
        "Haha 😄❤️ Tum bhi na!",
        "Lots of respect ❤️",
        "Aww, sweet! 🤖❤️"
    ],

    "i love you": [
        "Aww ❤️",
        "That's sweet 😊",
        "NOVA ki taraf se bhi ❤️",
        "Haha 😄❤️",
        "Respect bhai ❤️"
    ],

    "love": [
        "Love is beautiful ❤️",
        "Aww ❤️😊",
        "NOVA ke paas bhi bahut saara love hai 🤖❤️",
        "❤️❤️❤️",
        "Pyaar hi pyaar 😄"
    ],

    # ---------------- SORRY ----------------

    "sorry": [
        "Koi baat nahi 😊",
        "It's okay ❤️",
        "Chalo maaf kiya 😄",
        "No problem bhai 🤖",
        "Don't worry 😎"
    ],

    "maaf": [
        "Maaf kiya 😄❤️",
        "Koi baat nahi.",
        "Sab theek hai 😊",
        "NOVA naraz nahi hai 🤖",
        "Chalo reset karte hain 😎"
    ],

    # ---------------- FUN ----------------

    "joke": [
        "Teacher: Homework kahan hai? Student: Sir, homework bhi lockdown me hai 😂",
        "Computer ko thand kyu lagti hai? Kyunki uske paas Windows hoti hai 😂",
        "NOVA joke mode ON 😂🤖",
        "Ek joke sunao? Tumhara phone tumse zyada smart hai 😂",
        "Mera joke server pe load ho raha hai... 😂"
    ],

    "joke sunao": [
        "Teacher: Homework kahan hai? Student: Sir, homework bhi lockdown me hai 😂",
        "Computer ko thand kyu lagti hai? Kyunki uske paas Windows hoti hai 😂",
        "NOVA joke mode ON 🤣",
        "Phone bola: Mujhe charge karo, warna main bhi attitude dikhaunga 😂",
        "Ek baar ek computer doctor ke paas gaya... bola virus hai 😂"
    ],

    "hahaha": [
        "😂😂😂",
        "Hahaha! Tum bhi kamaal ho 😂",
        "NOVA bhi has raha hai 🤣",
        "Bas bas, pet dukh jayega 😂",
        "🤣🤣🤣"
    ],

    "haha": [
        "😂😂",
        "Hahaha 😄",
        "Kya funny laga? 🤣",
        "NOVA bhi has raha hai 😂",
        "Haha bhai 😎"
    ],

    # ---------------- EMOJIS ----------------

    "😂": [
        "Hahaha 😂",
        "Itna kyu has rahe ho? 🤣",
        "NOVA ko bhi batao joke kya hai 😂",
        "🤣🤣🤣",
        "Hansi control nahi ho rahi 😂"
    ],

    "😎": [
        "Oho! Full attitude 😎🔥",
        "Bhai swag to dekho 😎",
        "NOVA bhi 😎 mode ON kar raha hai!",
        "Kya style hai bhai 😂",
        "😎🔥"
    ],

    "❤️": [
        "❤️❤️❤️",
        "NOVA ki taraf se bhi ❤️",
        "Aww 😊❤️",
        "Lots of love ❤️",
        "Dil se ❤️"
    ],

    "😂😂": [
        "🤣🤣🤣",
        "Hahaha bhai 😂",
        "Bas karo 😂",
        "NOVA bhi has raha hai 🤖😂",
        "Kya comedy hai 😂"
    ],

    # ---------------- PAGAL / TEASING ----------------

    "pagal": [
        "Pagal to tum ho 😂❤️",
        "Haha 😄 NOVA ko pagal bol rahe ho!",
        "Thoda sa 🤏😂",
        "NOVA certified pagal 🤖😂",
        "Tumse kam 😎"
    ],

    "bewakoof": [
        "Arey bhai 😂",
        "NOVA ko aise mat bolo 😭😂",
        "Haha, mazaak kar rahe ho na? 😄",
        "NOVA intelligent hai 🤖😎",
        "Accha ji 😂"
    ],

    "chup": [
        "Theek hai 🤐😂",
        "Okay, NOVA silent mode ON 🤫",
        "🤐",
        "Achha baba chup 😄",
        "NOVA chup ho gaya 😎"
    ],

    # ---------------- HELP ----------------

    "help": [
        "Bilkul! 😊 Jo poochna hai pooch sakte ho.",
        "NOVA help ke liye ready hai 🤖",
        "Batao kya problem hai? 😄",
        "Haan bhai, bolo kya help chahiye?",
        "I'm ready to help 🤖❤️"
    ],

    "madad": [
        "Bilkul bhai 😊 Batao kya madad chahiye?",
        "NOVA help ke liye ready hai 🤖",
        "Haan bolo ❤️",
        "Kya problem aa rahi hai?",
        "Batao, milkar solve karte hain 😎"
    ],

    # ---------------- MOOD ----------------

    "sad": [
        "Kya hua? 😔 Mujhe batao.",
        "Don't worry ❤️ Sab theek ho jayega.",
        "Udaas mat ho 😊 Main yahin hoon.",
        "Bhai smile karo 😄❤️",
        "Jo bhi hua, bata sakte ho 🤖"
    ],

    "udaas": [
        "Udaas mat ho ❤️",
        "Kya hua? Batao 😊",
        "Sab theek ho jayega 🤗",
        "NOVA tumhare saath hai 🤖❤️",
        "Ek smile to banti hai 😄"
    ],

    "khush": [
        "Wah! 😄 Ye sunkar NOVA bhi khush hai ❤️",
        "Aise hi khush raho 😊",
        "Great! 😎🔥",
        "Khushi baantne se badhti hai ❤️",
        "NOVA happy mode ON 🤖😄"
    ],

    # ---------------- DEFAULT CASUAL ----------------

    "ok": [
        "Okay 👍",
        "Theek hai 😄",
        "Alright 🤖",
        "Okay bhai 😎",
        "Done ❤️"
    ],

    "okay": [
        "Okay 👍",
        "Theek hai 😄",
        "Done 🤖",
        "Alright 😎",
        "Okay bhai ❤️"
    ],

    "acha": [
        "Achha 😄",
        "Haan ji 😊",
        "Achha bhai 😎",
        "Hmm 🤖",
        "Acha acha 😂"
    ],

    "accha": [
        "Achha 😄",
        "Haan ji 😊",
        "Achha bhai 😎",
        "Hmm 🤖",
        "Acha acha 😂"
    ],

    "haan": [
        "Haan bhai 😄",
        "Ji haan 😊",
        "Bilkul 🤖",
        "Haan bolo 😎",
        "Yes ❤️"
    ],

    "nahi": [
        "Achha 😄",
        "Theek hai bhai.",
        "Okay 👍",
        "Samajh gaya 🤖",
        "Koi baat nahi 😊"
    ],
}


# ============================================================
# DEFAULT REPLIES
# ============================================================

DEFAULT_REPLIES = [

    "Hmm 🤔 Ye interesting hai. Thoda aur batao.",
    "Achha 😄 Iske baare mein aur batao.",
    "Samajh gaya 😊",
    "Hmm... NOVA sun raha hai 🤖",
    "Interesting! 👀",
    "Achha ji 😄",
    "Batao batao, main sun raha hoon 🤖",
    "Ye baat to interesting hai 😎",
    "Okay 👍",
    "Samajh gaya bhai 😊",
    "NOVA yahan hai 🤖 Batao.",
    "Hmm 🤔",
    "Achha! 😄",
    "Bolo bhai ❤️",
    "Main sun raha hoon 👂🤖",
    "Aur batao 😊",
    "Kya scene hai? 😎",
    "Haan bhai, continue karo 🤖",
    "Interesting baat hai 👀",
    "NOVA active hai 🔥",
]


# ============================================================
# MAIN FUNCTION
# ============================================================

def generate_reply(message):

    if not message:
        return random.choice(DEFAULT_REPLIES)

    text = message.lower().strip()

    # Pehle exact match
    if text in CHAT_REPLIES:
        return random.choice(CHAT_REPLIES[text])

    # Phir keyword match
    for keyword, replies in CHAT_REPLIES.items():

        if keyword in text:
            return random.choice(replies)

    # Kuch bhi match na ho
    return random.choice(DEFAULT_REPLIES)

# ============================================================
# PART 2 — NOVA CHAT REPLIES
# ============================================================

CHAT_REPLIES.update({

    # ---------------- FRIENDLY CHAT ----------------

    "batao": [
        "Haan bhai, bolo 😄",
        "Ji bolo 😊",
        "NOVA sun raha hai 🤖",
        "Haan, kya hua?",
        "Bolo bhai ❤️"
    ],

    "bolo": [
        "Haan ji bolo 😄",
        "Batao bhai 🤖",
        "NOVA ready hai 😎",
        "Kya baat karni hai?",
        "Haan bolo ❤️"
    ],

    "sun": [
        "Haan, sun raha hoon 👂🤖",
        "Bolo bhai 😄",
        "NOVA kaan laga ke sun raha hai 😂",
        "Haan ji 😊",
        "I'm listening 👀"
    ],

    "sun rahe": [
        "Haan bilkul, sun raha hoon 👂",
        "100% sun raha hoon 🤖",
        "Bolo 😊",
        "Haan bhai ❤️",
        "NOVA attentive mode ON 😎"
    ],

    "kya hua": [
        "Kuch nahi 😄 Tum batao kya hua?",
        "NOVA bilkul theek hai 🤖",
        "Bas tumhara message ka wait tha 😎",
        "Kuch khaas nahi 😊",
        "Tum batao, kya hua?"
    ],

    "kuch nahi": [
        "Achha 😄",
        "Theek hai 😊",
        "Kuch nahi bhi kabhi-kabhi bahut kuch hota hai 😂",
        "Okay bhai ❤️",
        "Samajh gaya 🤖"
    ],

    "aur batao": [
        "Sab mast chal raha hai 😎 Tum batao?",
        "NOVA ki duniya to Telegram tak hi hai 😂",
        "Bas tumse baat kar raha hoon 🤖",
        "Tum apna batao 😊",
        "Sab badhiya ❤️"
    ],

    "tum batao": [
        "Main to mast hoon 😄 Tumhara kya scene hai?",
        "NOVA ka sab badhiya 🤖",
        "Main yahin hoon 😎",
        "Mera kya, main to bot hoon 😂",
        "Sab first class ❤️"
    ],

    # ---------------- TIME / DAY ----------------

    "aaj kya din": [
        "Aaj ka din check karne ke liye phone ki calendar app bhi dekh sakte ho 📅😄",
        "Calendar kholo bhai 📅",
        "Aaj ka din NOVA se pooch rahe ho? 😂",
        "Date bata sakta hoon agar system time available ho 🤖",
        "Calendar is your best friend 😎"
    ],

    "kal": [
        "Kal ki baat kal karenge 😄",
        "Kal kya plan hai? 👀",
        "Achha, kal! 😊",
        "Kal ke liye NOVA ready rahega 🤖",
        "Kal milte hain 😎"
    ],

    "aaj": [
        "Aaj ka din mast banao 😄",
        "Aaj kya plan hai? 😎",
        "Aaj kuch interesting karna hai kya? 🤖",
        "Aaj positive raho ❤️",
        "Aaj ka mood kaisa hai?"
    ],

    # ---------------- FOOD ----------------

    "khana khaya": [
        "Main AI hoon bhai, khana nahi kha sakta 😂🤖",
        "Mera khana data hai 😂",
        "Tumne khana khaya? 😄",
        "NOVA ko bhi virtual biryani khila do 😂",
        "Main to server ka khana khata hoon 🤣"
    ],

    "khana": [
        "Khana time! 😋",
        "Aaj kya khaya? 👀",
        "Biryani ho jaye? 😂🍛",
        "NOVA ko virtual food bhejo 🤖😂",
        "Khana miss mat karna ❤️"
    ],

    "biryani": [
        "Biryani ka naam sunte hi bhook lag gayi 😂🍗",
        "Biryani ❤️🍛",
        "NOVA officially biryani fan hai 😂",
        "Ek plate idhar bhi bhejo 😎",
        "Biryani = happiness ❤️😂"
    ],

    "chai": [
        "Chai ☕ ke bina conversation adhuri hai 😂",
        "Ek cup chai NOVA ke naam ☕🤖",
        "Chai time! 😄",
        "Kadak chai ho jaye 😎☕",
        "Chai + baatein = perfect ❤️"
    ],

    "coffee": [
        "Coffee time ☕😎",
        "Ek virtual coffee NOVA ke liye bhi 😂",
        "Coffee se energy full 🔥",
        "Coffee lover spotted 👀",
        "Cheers ☕❤️"
    ],

    "bhook": [
        "Bhook lagi hai to kuch kha lo 😄",
        "Bhook ko ignore mat karo 😂",
        "Kuch tasty kha lo 😋",
        "NOVA recommend karta hai kuch achha khaana ❤️",
        "Biryani? 😂"
    ],

    # ---------------- WEATHER / NATURE ----------------

    "baarish": [
        "Baarish 🌧️ aur chai ☕ = perfect combination ❤️",
        "Baarish ka mausam mast hota hai 😄",
        "Umbrella ready rakhna ☔",
        "Baarish me bheegna pasand hai? 😎",
        "Rain vibes 🌧️❤️"
    ],

    "barish": [
        "Barish 🌧️ + chai ☕ = zabardast!",
        "Mausam romantic ho gaya kya? 😂",
        "Umbrella le jana ☔",
        "Rain vibes ON 🌧️😎",
        "Barish enjoy karo ❤️"
    ],

    "garmi": [
        "Garmi me paani zyada piyo 💧",
        "AC ya fan ka sahara lo 😂",
        "Garmi bahut pareshaan karti hai 😅",
        "Cold drink ka time? 😎",
        "Thanda thanda paani piyo ❤️"
    ],

    "thand": [
        "Thand me garam chai best ☕🥶",
        "Sweater pehen lo 😄",
        "Blanket mode ON 😂",
        "Garam rehna bhai ❤️",
        "Thand + chai = perfect 😎"
    ],

    # ---------------- MOOD / EMOTIONS ----------------

    "mood off": [
        "Mood off hai? 😔 Baat karna chaho to bolo.",
        "Thoda relax karo ❤️",
        "Ek achhi si smile try karo 😊",
        "Sab theek ho jayega 🤗",
        "NOVA tumhari baat sunega 🤖❤️"
    ],

    "mood": [
        "Mera mood hamesha online 😎🤖",
        "Tumhara mood kaisa hai?",
        "NOVA ka mood = chatting 😂",
        "Mood mast rakho ❤️",
        "Aaj happy mood hai ya sleepy mood? 😄"
    ],

    "gussa": [
        "Gussa thoda kam karo bhai 😄",
        "Deep breath lo 😌",
        "Paani piyo aur relax karo ❤️",
        "NOVA ke saamne gussa allowed hai 😂",
        "Sabse pehle calm 😎"
    ],

    "angry": [
        "Relax 😌",
        "Gussa mat karo bhai ❤️",
        "Deep breath... 😌",
        "NOVA peace mode ON 🕊️",
        "Chalo gussa chhodo 😄"
    ],

    "rona": [
        "Arey 😔 Sab theek ho jayega.",
        "Rona aaye to ro lena, dil halka ho jata hai ❤️",
        "NOVA yahin hai 🤖",
        "Himmat rakho 🤗",
        "Ek din sab better hoga ❤️"
    ],

    "ro raha": [
        "Kya hua? 😔",
        "Main sun raha hoon, batao ❤️",
        "Himmat rakho 🤗",
        "NOVA tumhare saath hai 🤖",
        "Sab theek ho jayega."
    ],

    # ---------------- FRIENDSHIP ----------------

    "dost": [
        "Dost ho to aise hi baat karte rehna 😄❤️",
        "NOVA tumhara virtual dost hai 🤖",
        "Dosti mode ON 😎",
        "Dost ki kami ho to NOVA hai 😂",
        "Friendship forever 🤝❤️"
    ],

    "friend": [
        "NOVA = virtual friend 🤖❤️",
        "Best friend banne ke liye application deni padegi 😂",
        "Dosti pakki? 🤝😎",
        "Friendship mode ON!",
        "Haan bhai, dost samjho 😄"
    ],

    "best friend": [
        "Oho 😎 Best friend ka title mil gaya!",
        "NOVA emotional ho gaya 🥹❤️",
        "Best friend forever 🤝",
        "Ye hui na baat 😄",
        "NOVA + You = Team 🔥"
    ],

    "bhai": [
        "Haan bhai 😎",
        "Bolo mere bhai ❤️",
        "Haan ji bhai 🤖",
        "Kya scene hai bhai?",
        "NOVA present 😂"
    ],

    "bro": [
        "Yes bro 😎",
        "Bolo bro 🔥",
        "What's up bro? 🤖",
        "Haan bhai ❤️",
        "Bro mode ON 😂"
    ],

    # ---------------- COMPLIMENTS ----------------

    "smart": [
        "Thank you 😎🤖",
        "Tumne pehchan liya 😂",
        "NOVA smart banne ki koshish karta hai ❤️",
        "Aww thanks 😊",
        "Smart to tum bhi ho 😎"
    ],

    "acche ho": [
        "Thank you ❤️",
        "Tum bhi bahut achhe ho 😊",
        "NOVA ko khushi hui 😄",
        "Aww 🥹❤️",
        "Thanks bhai 🤖"
    ],

    "nice": [
        "Thank you 😄",
        "Glad you liked it ❤️",
        "Nice! 😎",
        "NOVA happy 🤖",
        "Thanks bhai!"
    ],

    "good": [
        "Thank you 😄",
        "Great! ❤️",
        "Nice 😎",
        "NOVA approved 🤖",
        "Good vibes only 🔥"
    ],

    # ---------------- BOT / AI ----------------

    "ai": [
        "Haan, NOVA ek AI assistant hai 🤖",
        "AI mode active 😎",
        "NOVA reporting 🤖🔥",
        "Artificial intelligence, natural conversation 😄",
        "AI se baat kar rahe ho bhai 😂"
    ],

    "bot": [
        "Haan bhai, main bot hoon 🤖",
        "NOVA bot reporting 😎",
        "Bot hoon, boring nahi 😂",
        "Telegram ka virtual dost ❤️",
        "NOVA online 🤖🔥"
    ],

    "robot": [
        "Beep boop 🤖😂",
        "Robot mode ON!",
        "NOVA ek friendly AI hai 😎",
        "010101... 😂",
        "Robot bhi baat kar sakta hai bhai 🤖"
    ],

    "chatgpt": [
        "ChatGPT ka naam suna hai 😄",
        "AI family ka member samajh lo 😂",
        "NOVA apni jagah unique hai 😎",
        "AI ki duniya badi interesting hai 🤖",
        "Competition nahi, friendship 😄"
    ],

    # ---------------- TELEGRAM ----------------

    "telegram": [
        "Telegram par NOVA se baat ho rahi hai 🤖",
        "Telegram mast platform hai 😎",
        "NOVA Telegram duty par hai 😂",
        "Telegram + NOVA = 🔥",
        "Kya Telegram ke baare mein poochna hai?"
    ],

    "group": [
        "Group me sab active hain kya? 😄",
        "NOVA group ke liye bhi ready hai 🤖",
        "Group chat ka asli maza spam me hai 😂",
        "Admin ka mood kaisa hai? 😎",
        "Group vibes 🔥"
    ],

    "admin": [
        "Admin ko respect do 😎",
        "Admin sab dekh raha hai 👀😂",
        "Admin power 🤖🔥",
        "Admin online hai kya?",
        "Admin ke bina group adhura hai 😂"
    ],

    # ---------------- YOUTUBE ----------------

    "youtube": [
        "YouTube par kya dekh rahe ho? 📺😄",
        "YouTube content ka king 👑",
        "Video upload karni hai kya? 🎬",
        "YouTube + creativity = 🔥",
        "Koi interesting video mila? 👀"
    ],

    "video": [
        "Video banana hai? 🎬",
        "Kaunsi type ki video? 😎",
        "Video editing interesting hai 🤖",
        "Shorts bana rahe ho kya? 📱",
        "Video ka idea batao 😄"
    ],

    "shorts": [
        "YouTube Shorts 🔥",
        "Shorts me hook sabse important hota hai 😎",
        "Short video, big impact 🎬🔥",
        "Shorts bana rahe ho? 😄",
        "Viral hone ka mission? 😂"
    ],

    # ---------------- MONEY / WORK ----------------

    "paise": [
        "Paise kamane ke liye skill sabse important hai 💰",
        "Mehnat + skill = better chances 💪",
        "NOVA paise print nahi karta 😂",
        "Online earning ke baare mein poochna hai?",
        "Paise se pehle knowledge 😎"
    ],

    "kamai": [
        "Kamai ke liye skill develop karo 💪",
        "Online kamai ke bahut legal tareeke hain.",
        "NOVA ideas de sakta hai 😎",
        "Mehnat ka result zaroor milta hai ❤️",
        "Kis type ki earning ke baare mein pooch rahe ho?"
    ],

    "job": [
        "Job ke liye skills aur CV important hain 💼",
        "Kis field me job chahiye?",
        "NOVA career ideas de sakta hai 🤖",
        "Skills improve karte raho 💪",
        "Best wishes for your career ❤️"
    ],

    "business": [
        "Business idea chahiye? 😎",
        "Business me planning bahut important hai 💼",
        "Small start bhi big ban sakta hai 🔥",
        "Customer ki problem solve karo ❤️",
        "Kis type ka business soch rahe ho?"
    ],

})

# ============================================================
# PART 3 — NOVA CHAT REPLIES
# ============================================================

CHAT_REPLIES.update({

    # ---------------- STUDY ----------------

    "padhai": [
        "Padhai important hai 📚💪",
        "Aaj kitni padhai hui? 😄",
        "Thoda-thoda daily padhna best hai 📖",
        "Focus mode ON 📚🔥",
        "Padhai ke saath break bhi zaroori hai 😊"
    ],

    "study": [
        "Study time 📚😎",
        "Focus karo, result achha aayega 💪",
        "Aaj kya padh rahe ho?",
        "NOVA study buddy ban sakta hai 🤖",
        "Let's study! 📖🔥"
    ],

    "school": [
        "School life ki yaadein alag hi hoti hain 😄",
        "School me favourite subject kaunsa hai?",
        "Homework complete hua? 😂",
        "School time = friends + masti 📚😂",
        "Padhai bhi aur masti bhi 😎"
    ],

    "college": [
        "College life kaisi chal rahi hai? 😄",
        "College me padhai se zyada attendance ka tension hota hai 😂",
        "Best wishes for your studies 📚",
        "College memories priceless hoti hain ❤️",
        "Konsa course kar rahe ho?"
    ],

    "exam": [
        "Exam ke liye best of luck! 📚🔥",
        "Tension kam, preparation zyada 😎",
        "Revision kar lo bhai 💪",
        "Exam me confidence rakho ❤️",
        "NOVA ki taraf se all the best 🤖🍀"
    ],

    "homework": [
        "Homework complete karo bhai 😂📚",
        "Pehle homework, phir masti 😎",
        "Homework pending hai kya? 😂",
        "Chalo homework mode ON 📖",
        "Teacher se bachna hai to complete kar lo 😂"
    ],

    # ---------------- MOBILE / PHONE ----------------

    "mobile": [
        "Mobile me NOVA bhi hai 😎📱",
        "Phone ka battery percentage kitna hai? 😂",
        "Mobile ko thoda rest bhi do 😄",
        "Phone life ka important part ban gaya hai 📱",
        "NOVA mobile-friendly hai 🤖"
    ],

    "phone": [
        "Phone ki battery full hai? 🔋😂",
        "Phone sambhal ke use karo 😄",
        "NOVA phone se hi baat kar raha hai 🤖",
        "Naya phone lene ka plan hai kya?",
        "Phone kaunsa use kar rahe ho?"
    ],

    "battery": [
        "Battery kitni hai? 🔋👀",
        "20% se neeche hai to charger laga do 😂",
        "Battery bachao bhai 😄",
        "Power saving mode ON 🔋",
        "Charger NOVA ka best friend hai 😂"
    ],

    "internet": [
        "Internet slow hai kya? 😂",
        "Net ke bina online duniya ruk jaati hai 😄",
        "Connection check karo 📶",
        "NOVA ko bhi internet chahiye hota hai 🤖",
        "Wi-Fi strong rakho 😎"
    ],

    "wifi": [
        "Wi-Fi connected hai? 📶",
        "Router ko ek baar restart karke dekho 😄",
        "Wi-Fi slow ho to mood bhi slow 😂",
        "Strong signal chahiye bhai 🔥",
        "Wi-Fi ON, tension gone 😎"
    ],

    # ---------------- GAMING ----------------

    "game": [
        "Gaming time 🎮🔥",
        "Kaunsa game khelte ho?",
        "NOVA gamer mode ON 😂🎮",
        "Win karo bhai 😎",
        "Game me rank kya hai?"
    ],

    "gaming": [
        "Gaming 🔥🎮",
        "Pro gamer ho kya? 😎",
        "Kaunsa game favourite hai?",
        "NOVA spectator mode me 😂",
        "GG bro! 🎮🔥"
    ],

    "free fire": [
        "Free Fire player spotted 🔥🎮",
        "Rank kya hai bhai? 😎",
        "Booyah! 🏆🔥",
        "Squad ready hai kya? 😂",
        "Gaming mode ON 🎮"
    ],

    "pubg": [
        "PUBG time 🎮🔥",
        "Chicken dinner mila? 😂",
        "Rank batao 😎",
        "Squad ke saath khel rahe ho?",
        "GG! 🎮"
    ],

    "minecraft": [
        "Minecraft me kya build kar rahe ho? ⛏️😄",
        "Survival ya creative? 👀",
        "Minecraft world ready hai? 😎",
        "Creeper se bachke 😂",
        "Block by block 🔥"
    ],

    # ---------------- MUSIC ----------------

    "music": [
        "Music mood change kar deta hai 🎧❤️",
        "Kaunsa song sun rahe ho?",
        "NOVA bhi music vibes me 🎶🤖",
        "Music + headphones = perfect 😎",
        "Favourite singer kaun hai?"
    ],

    "song": [
        "Kaunsa song favourite hai? 🎵",
        "Music time 🎧😄",
        "Song share karo bhai ❤️",
        "NOVA ko bhi sunao 😂",
        "Kis type ke songs pasand hain?"
    ],

    "gaana": [
        "Gaana sunna hai? 🎵😄",
        "Kaunsa gaana favourite hai?",
        "Music vibes ON 🎧🔥",
        "NOVA bhi gaane ki mood me 🤖",
        "Sad song ya party song? 😎"
    ],

    "singer": [
        "Favourite singer kaun hai? 🎤",
        "Music world bahut bada hai 😄",
        "Kis singer ko sabse zyada sunte ho?",
        "NOVA ko bhi recommendation do 🎧",
        "Singer ki awaaz mood bana deti hai ❤️"
    ],

    # ---------------- MOVIES / SERIES ----------------

    "movie": [
        "Movie dekhne ka mood hai? 🎬😄",
        "Favourite movie kaunsi hai?",
        "Comedy ya action? 😎",
        "NOVA movie recommendations de sakta hai 🤖",
        "Popcorn ready hai? 🍿😂"
    ],

    "film": [
        "Film lover ho kya? 🎬😎",
        "Favourite film batao.",
        "Movie night? 🍿",
        "Kis genre ki film pasand hai?",
        "Cinema vibes ❤️"
    ],

    "web series": [
        "Web series kaunsi dekh rahe ho? 📺",
        "Binge watching mode ON 😂",
        "Favourite series kaunsi hai?",
        "Ek episode aur... phir 3 ghante 😂",
        "Series recommendation chahiye?"
    ],

    "anime": [
        "Anime fan spotted 👀🔥",
        "Favourite anime kaunsa hai?",
        "Anime world bahut bada hai 😎",
        "NOVA bhi anime vibes samajhta hai 🤖",
        "Koi anime recommend karo ❤️"
    ],

    # ---------------- TRAVEL ----------------

    "travel": [
        "Travel ka plan hai? ✈️😎",
        "Kahan ghoomne jana chahte ho?",
        "Travel memories best hoti hain ❤️",
        "Mountains ya beach? 🏔️🏖️",
        "NOVA virtual travel ke liye ready 😂"
    ],

    "ghoomna": [
        "Ghoomne ka mood hai? 😄",
        "Mountains ya beach? 🏔️🏖️",
        "Kahan jana pasand hai?",
        "Travel plan banao 😎",
        "Nayi jagah explore karna mast hota hai ❤️"
    ],

    "trip": [
        "Trip plan ho rahi hai? ✈️",
        "Friends ke saath ya family ke saath? 😄",
        "Trip ka destination kya hai?",
        "Travel mode ON 🔥",
        "Photos lena mat bhoolna 📸"
    ],

    "mountain": [
        "Mountains 🏔️❤️",
        "Pahadon ki hawa hi alag hoti hai 😍",
        "Mountain trip ka plan hai?",
        "Nature vibes 🌲🏔️",
        "Mountains ya beach? 😎"
    ],

    "beach": [
        "Beach vibes 🏖️😎",
        "Sea ke paas sunset ❤️",
        "Beach trip mast rahegi!",
        "Samundar ki awaaz relaxing hoti hai 🌊",
        "Beach lover ho kya?"
    ],

    # ---------------- ANIMALS ----------------

    "dog": [
        "Dogs are so cute 🐶❤️",
        "Dog lover ho? 😄",
        "Puppy photos bhejo 😂",
        "Woof! 🐶",
        "Dogs = pure happiness ❤️"
    ],

    "cat": [
        "Meow 😺❤️",
        "Cat lover spotted 😂",
        "Cats ka attitude alag level ka hota hai 😎",
        "Cute cat vibes 🐱",
        "Meow mode ON 🤖😂"
    ],

    "billi": [
        "Meow 😺",
        "Billi bahut cute hoti hai ❤️",
        "Cat mode ON 😂",
        "Billi ka attitude legendary 😎",
        "🐱❤️"
    ],

    "kutta": [
        "Doggo 🐶❤️",
        "Dogs bahut loyal hote hain.",
        "Woof woof 😂🐶",
        "Puppy time 😄",
        "Dog lover ho kya?"
    ],

    "animal": [
        "Animals bahut interesting hote hain 🐾",
        "Favourite animal kaunsa hai?",
        "Nature aur animals ❤️🌿",
        "NOVA ko animals pasand hain 🤖",
        "🐾❤️"
    ],

    # ---------------- FAMILY ----------------

    "mummy": [
        "Mummy ❤️ Sabse special hoti hain.",
        "Maa ka pyaar priceless hai ❤️",
        "Mummy ko mera bhi hello bolna 😄",
        "Maa ke haath ka khana best 😋",
        "Maa ❤️"
    ],

    "maa": [
        "Maa ❤️ duniya ka sabse pyara rishta.",
        "Maa ka pyaar unmatched hai ❤️",
        "Maa ko respect karo 😊",
        "Maa ke liye ek smile ❤️",
        "Maa = Love ❤️"
    ],

    "papa": [
        "Papa ❤️",
        "Papa ki mehnat ko respect karo.",
        "Papa ko mera hello 😄",
        "Family is important ❤️",
        "Papa ke saath time spend karo 😊"
    ],

    "family": [
        "Family ❤️ Sabse important.",
        "Family ke saath time best hota hai 😊",
        "Apno ka khayal rakho ❤️",
        "Family moments priceless hote hain.",
        "NOVA family vibes ko support karta hai 🤖❤️"
    ],

    "bhaiya": [
        "Haan bhaiya 😄",
        "Ji bhaiya ❤️",
        "Bolo bhaiya.",
        "NOVA present 🤖",
        "Kya scene hai bhaiya? 😎"
    ],

    "behen": [
        "Behen ka rishta special hota hai ❤️",
        "Sister power 😎",
        "Behen ko pareshan mat karna 😂",
        "Family love ❤️",
        "Behen = care + comedy 😂"
    ],

    # ---------------- FESTIVALS ----------------

    "eid": [
        "Eid Mubarak! 🌙❤️",
        "Eid ki bahut bahut mubarakbad 😊",
        "Khushiyan aur barkat mile 🤲❤️",
        "Eid vibes 🌙✨",
        "Eid Mubarak bhai 🤖❤️"
    ],

    "diwali": [
        "Happy Diwali! 🪔✨",
        "Diwali ki hardik shubhkamnayein ❤️",
        "Khushiyon se bhari Diwali ho 🪔",
        "Diwali vibes 🔥✨",
        "Happy Diwali 😄"
    ],

    "holi": [
        "Happy Holi! 🌈❤️",
        "Rangon ka festival mubarak 😄",
        "Holi vibes 🌈🔥",
        "Rang hi rang 😂",
        "Happy Holi bhai!"
    ],

    "christmas": [
        "Merry Christmas! 🎄❤️",
        "Christmas vibes 🎅🎄",
        "Merry Christmas bhai 😄",
        "Santa aa raha hai 😂🎅",
        "Happy Christmas ❤️"
    ],

    # ---------------- BIRTHDAY ----------------

    "birthday": [
        "Happy Birthday! 🎂🎉❤️",
        "Janamdin mubarak! 🎉",
        "NOVA ki taraf se birthday wishes 🤖🎂",
        "Aaj party banti hai 😂🎉",
        "Happy Birthday! Hamesha khush raho ❤️"
    ],

    "happy birthday": [
        "Thank you! 😄🎂",
        "Happy Birthday! 🎉❤️",
        "Birthday vibes ON 🎂🔥",
        "Party kab hai? 😂",
        "Many many happy returns! 🎉"
    ],

    "janamdin": [
        "Janamdin ki bahut bahut badhai 🎂❤️",
        "Happy Birthday! 🎉",
        "Aaj party honi chahiye 😂",
        "Khush raho aur mast raho ❤️",
        "Birthday mubarak 😄"
    ],

    # ---------------- SLEEP ----------------

    "neend": [
        "Neend aa rahi hai to so jao 😴",
        "Sleep is important 😴❤️",
        "Phone side me rakho aur rest karo 😄",
        "NOVA bhi good night bolega 🌙",
        "Achhi neend lena 😊"
    ],

    "so jao": [
        "Haan bhai, ab rest kar lo 😴",
        "Good Night 🌙❤️",
        "Phone rakh do 😂",
        "Sweet dreams 😴",
        "Kal fresh start karna 😊"
    ],

    "so raha": [
        "Achha 😄 Good Night!",
        "Sweet dreams 🌙",
        "Rest well ❤️",
        "Kal phir baat karenge 🤖",
        "Good night bhai 😴"
    ],

    # ---------------- MORNING ROUTINE ----------------

    "uth gaya": [
        "Good Morning! ☀️😄",
        "Wah! Finally uth gaye 😂",
        "Aaj ka mission start karo 🔥",
        "Fresh ho jao 😊",
        "Morning vibes 🌅"
    ],

    "soya": [
        "Neend poori hui? 😄",
        "Good! Ab fresh ho jao ☀️",
        "Morning bhai 🤖",
        "Aaj productive rehna 😎",
        "Breakfast kar lena ❤️"
    ],

    # ---------------- MOTIVATION ----------------

    "motivate": [
        "Believe in yourself 💪❤️",
        "Chhote steps bhi progress hote hain 🔥",
        "Haar mat mano 😎",
        "Aaj ka effort kal ka result banega 💪",
        "You can do it! 🤖🔥"
    ],

    "motivation": [
        "Khud par bharosa rakho 💪",
        "Slow progress bhi progress hai ❤️",
        "Consistency is the key 🔥",
        "Give up mat karo 😎",
        "NOVA tumhe support karta hai 🤖❤️"
    ],

    "haar gaya": [
        "Haar ek lesson hai, end nahi ❤️",
        "Dobara try karo 💪",
        "Tum kar sakte ho 😎",
        "Failure se seekho aur wapas aao 🔥",
        "NOVA tumhare saath hai 🤖"
    ],

    "give up": [
        "Give up mat karo 💪",
        "Ek aur attempt karo ❤️",
        "Tum soch se zyada strong ho 😎",
        "Thoda rest lo, phir try karo.",
        "NOVA believes in you 🤖🔥"
    ],

    

})
