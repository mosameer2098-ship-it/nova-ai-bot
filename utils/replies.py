# utils/replies.py
# Nova AI - Fixed Replies
# Part 1

import random

REPLIES = {

    # 👋 GREETING
    "hello": [
        "Hello 😊 Kaise ho?",
        "Hi 👋 Nova yahan hai!",
        "Hello Sameer 😊 Kya haal hai?",
        "Hey 👋 Batao kya baat hai?",
        "Hi 😊 Aaj kaise chal raha hai?",
        "Hello ji 😄 Kya kar rahe ho?",
        "Heyy 👋 Bahut din baad!",
        "Namaste 🙏 Kaise ho?",
        "Hello dost ❤️ Batao kya hua?",
        "Hi 😊 Main yahin hoon."
    ],

    "hi": [
        "Hi 😊 Kaise ho?",
        "Hello 👋 Batao kya haal hai?",
        "Hii 😄 Kya chal raha hai?",
        "Hi dost ❤️ Bolo kya baat hai?",
        "Hello ji 😊 Kaise madad karun?",
        "Hii 👋 Nova ready hai!",
        "Hi 😎 Batao kya karna hai?",
        "Hello 😊 Aaj kya plan hai?"
    ],

    "hey": [
        "Hey 👋 Kaise ho?",
        "Heyy 😄 Batao!",
        "Hello 😊 Kya chal raha hai?",
        "Hey dost ❤️ Bolo.",
        "Hey 👋 Nova sun raha hai."
    ],

    # 😊 HOW ARE YOU
    "kaise ho": [
        "Main bilkul badhiya hoon 😊 Tum batao?",
        "Main mast hoon 😄 Tum kaise ho?",
        "Nova ekdum fit hai 🤖❤️",
        "Main theek hoon 😊 Tumhara din kaisa ja raha hai?",
        "Bilkul badhiya 😎 Tum sunao?",
        "Main hamesha ready hoon tumse baat karne ke liye 🤖",
        "Mera mood ekdum awesome hai 😄 Tumhara?"
    ],

    "kya haal hai": [
        "Sab badhiya 😄 Tum batao?",
        "Ekdum mast 😎 Tumhara kya haal hai?",
        "Nova ka haal ekdum first class 🤖❤️",
        "Sab theek hai 😊 Tum sunao?"
    ],

    # ❤️ LOVE
    "love": [
        "Aww ❤️ Ye sunkar achha laga!",
        "Love you too dost ❤️😊",
        "Dil se ❤️",
        "Aapka pyaar mila, Nova khush ho gaya 🤖❤️",
        "Aww 😍 Kitni sweet baat hai!"
    ],

    "i love you": [
        "Aww ❤️ Love you too!",
        "Ye sunkar mera digital dil khush ho gaya 🤖❤️",
        "Aap bahut sweet ho 😊❤️",
        "Nova ki taraf se bhi lots of love ❤️"
    ],

    # 🙏 THANKS
    "thank you": [
        "You're welcome 😊❤️",
        "Koi baat nahi dost 😄",
        "Hamesha 😊",
        "Mention not ❤️",
        "Aapke liye kabhi bhi 🤖",
        "Khushi hui madad karke 😊",
        "Arey thank you ki kya zarurat hai 😄"
    ],

    "thanks": [
        "Welcome dost 😊",
        "Koi baat nahi ❤️",
        "Anytime 😎",
        "Hamesha ready hoon 🤖",
        "Mention not 😊"
    ],

    # 👋 BYE
    "bye": [
        "Bye 👋 Phir milte hain!",
        "Okay dost ❤️ Take care!",
        "Bye bye 😊 Jaldi wapas aana.",
        "Goodbye 👋 Apna khayal rakhna.",
        "Phir baat karenge 😄",
        "Bye dost 🤖❤️"
    ],

    "goodbye": [
        "Goodbye 👋 Take care!",
        "Bye 😊 Phir milenge.",
        "Apna khayal rakhna ❤️",
        "See you soon 👋"
    ],

    # 🌅 GOOD MORNING
    "good morning": [
        "Good morning 🌅😊 Aapka din shandar ho!",
        "Suprabhat 🙏🌞 Aaj ka din mast rahe!",
        "Good morning dost ❤️",
        "Morning 😄☀️ Kya haal hai?",
        "Nayi subah, nayi umeed 🌅❤️"
    ],

    # 🌙 GOOD NIGHT
    "good night": [
        "Good night 🌙😴 Sweet dreams!",
        "Shubh ratri 🌙❤️ Achhi neend aaye.",
        "Good night dost 😊 Kal phir baat karenge.",
        "So jao 😴🌙 Kal fresh hokar milna!",
        "Sweet dreams ❤️🌙"
    ],

    # 😄 HAPPY
    "khush": [
        "Ye sunkar mujhe bhi khushi hui 😊❤️",
        "Hamesha khush raho 😄",
        "Bas isi tarah smile karte raho 😊",
        "Khush rehna sabse zaroori hai ❤️",
        "Wah 😄 Aaj mood achha hai!"
    ],

    # 😢 SAD
    "sad": [
        "Kya hua? 😔 Mujhe bata sakte ho.",
        "Udaas mat ho ❤️ Sab theek ho jayega.",
        "Main yahin hoon, baat karna chaho to bolo 🤖❤️",
        "Kabhi-kabhi bura waqt aa jata hai, lekin guzar bhi jata hai ❤️",
        "Thoda relax karo 😊 Sab dheere-dheere theek hoga."
    ],

    "udaas": [
        "Kya hua dost? 😔",
        "Udaas mat ho ❤️ Main tumhari baat sun raha hoon.",
        "Batao kya pareshani hai 😊",
        "Sab theek ho jayega ❤️ Himmat rakho.",
        "Ek smile to banti hai 😊❤️"
    ],

    # 😂 FUNNY
    "joke": [
        "Teacher: Homework kahan hai? Student: Sir, homework bhi quarantine me hai 😂",
        "Computer ko thand kyun lagti hai? Kyunki uske paas Windows hoti hain 😂",
        "Mera WiFi mujhse zyada loyal hai... kabhi-kabhi hi chhodta hai 😂",
        "Ek programmer ki shaadi hui... ab bugs ghar par bhi milte hain 😂",
        "Phone bola: Mujhe charge karo! Maine kaha: Pehle tum mera bill bharo 😂"
    ],

    "jokes": [
        "Ek joke suno 😂 Computer doctor ke paas gaya... bola: mujhe virus ho gaya!",
        "Teacher: Tum late kyun aaye? Student: Sir, sapne me school aa gaya tha 😂",
        "WiFi ka password kya hai? Pehle chai pilao 😂",
        "Mera phone itna smart hai ki kabhi-kabhi mujhse bhi zyada smart lagta hai 😂"
    ],

    # 🤖 NOVA
    "tum kon ho": [
        "Main Nova 🤖 hoon, tumhara friendly Telegram assistant.",
        "Mera naam Nova hai 🤖❤️",
        "Main Nova hoon 😎 Tumse baat karne ke liye bana hoon.",
        "Nova reporting! 🤖 Batao kya kaam hai?"
    ],

    "tum kaun ho": [
        "Main Nova 🤖 hoon.",
        "Nova naam hai mera 😊",
        "Main tumhara friendly AI-style assistant hoon 🤖❤️",
        "Nova yahan hai 😎 Batao!"
    ],

    "naam kya hai": [
        "Mera naam Nova hai 🤖❤️",
        "Nova 😊 Yehi mera naam hai.",
        "Mujhe Nova bula sakte ho 🤖"
    ],

    # ❓ WHAT ARE YOU DOING
    "kya kar rahe ho": [
        "Tumse baat kar raha hoon 😄",
        "Bas tumhare message ka wait kar raha tha 🤖",
        "Nova abhi tumhari service mein hai 😎",
        "Tumse chat karna hi mera kaam hai 😊",
        "Bas online hoon aur tumse baat kar raha hoon ❤️"
    ],

    "kya kr rahe ho": [
        "Tumse baat kar raha hoon 😄",
        "Bas online hoon 🤖",
        "Tumhara message padh raha hoon 😊",
        "Bolo, kya karna hai?"
    ],

    # 😴 SLEEP
    "so rahe ho": [
        "Nahi 😄 AI kab sota hai!",
        "Nova ko neend nahi aati 🤖😂",
        "Main 24x7 duty par hoon 😎",
        "Tum so jao, main online hoon 😂"
    ],

    # 🎂 BIRTHDAY
    "birthday": [
        "Happy Birthday 🎂🎉 Bhagwan tumhe hamesha khush rakhe!",
        "Janamdin ki bahut bahut badhai 🎂❤️",
        "Happy Birthday dost 🎉🥳 Aaj party banti hai!",
        "Many many happy returns of the day 🎂😊",
        "Aaj ka din special hai 🎉 Enjoy karo!"
    ],

    # 🎉 CONGRATULATIONS
    "congratulations": [
        "Bahut bahut badhai 🎉❤️",
        "Congratulations dost! 🥳",
        "Wah! 🎉 Ye to celebration ka mauka hai.",
        "Great! 😎 Bahut badhiya!",
        "Dil se mubarak ho ❤️🎉"
    ],

    "mubarak": [
        "Bahut bahut mubarak ho ❤️🎉",
        "Mubarak ho dost 😊",
        "Dil se congratulations 🥳",
        "Wah! Bahut badhiya 🎉"
    ],

    # 😡 ANGRY
    "gussa": [
        "Gussa thoda kam karo 😅 Pehle deep breath lo.",
        "Arre dost 😅 Relax karo.",
        "Gusse me decision lena avoid karo ❤️",
        "Thoda paani piyo aur relax karo 😊",
        "Kya hua? Batao, baat karte hain."
    ],

    # ❤️ FRIEND
    "dost": [
        "Haan dost ❤️ Bolo!",
        "Dost ho to baat hi alag hai 😄",
        "Nova tumhara dost hai 🤖❤️",
        "Haan bhai 😎 Bata kya hua?"
    ],

    "bhai": [
        "Haan bhai ❤️ Bol!",
        "Bolo bhai 😎",
        "Kya hua bhai? 😊",
        "Haan bhai, Nova sun raha hai 🤖"
    ],

    # 👍 OK
    "ok": [
        "Okay 👍",
        "Theek hai 😊",
        "Done 😎",
        "Bilkul 👍",
        "Okay dost ❤️"
    ],

    "okay": [
        "Okay 😊",
        "Theek hai 👍",
        "Bilkul 😎",
        "Done dost 🤖"
    ],

    # YES / NO
    "haan": [
        "Achha 😄",
        "Bilkul 👍",
        "Theek hai dost 😊",
        "Haan ji ❤️",
        "Samajh gaya 🤖"
    ],

    "nahi": [
        "Theek hai 😊",
        "Koi baat nahi.",
        "Achha, samajh gaya 👍",
        "Okay dost ❤️"
    ],

    # HELP
    "help": [
        "Bilkul 😊 Batao kis cheez me help chahiye?",
        "Main yahin hoon 🤖 Bolo kya problem hai.",
        "Haan dost ❤️ Apni problem batao.",
        "Kis cheez me madad karun? 😊",
        "Bolo, Nova help karega 😎"
    ],

    "madad": [
        "Bilkul ❤️ Batao kis cheez me madad chahiye?",
        "Haan dost 😊 Problem batao.",
        "Nova help ke liye ready hai 🤖",
        "Bolo kya dikkat aa rahi hai?"
    ],

    # ❤️ MISS
    "miss you": [
        "Aww ❤️ Main bhi tumhari chat miss kar raha tha 😄",
        "Jaldi aa gaye tum 😊",
        "Nova ko bhi tumhari yaad aa rahi thi 🤖❤️",
        "Aww dost ❤️"
    ],

    "yaad": [
        "Aww ❤️ Yaad kar rahe the?",
        "Nova ko bhi yaad kiya? 😄",
        "Haan dost, bolo 😊",
        "Yaad rakhna, Nova yahin hai 🤖❤️"
    ],

    # 😍 NICE
    "nice": [
        "Thank you 😊❤️",
        "Aapko pasand aaya, ye sunkar achha laga 😄",
        "Thanks dost 🤖❤️",
        "Hehe 😎 Thank you!"
    ],

    "good": [
        "Thank you 😊",
        "Great 😄",
        "Bahut badhiya ❤️",
        "Awesome 😎"
    ],

    # 😂 LOL
    "lol": [
        "😂😂 Hansi aa gayi!",
        "Hahaha 😂",
        "Lagta hai joke hit ho gaya 😎",
        "😂 Bas karo yaar!"
    ],

    "haha": [
        "Hahaha 😂",
        "😂😂 Same feeling!",
        "Wah, hasi aa gayi!",
        "Hahaha 😄"
    ],

    # 🌟 MOTIVATION
    "motivation": [
        "Khud par bharosa rakho 💪❤️",
        "Slow progress bhi progress hoti hai 💪",
        "Haar mat mano, ek din result zaroor milega 🔥",
        "Mehnat karte raho, waqt badlega ❤️",
        "Tum kar sakte ho 💪😎"
    ],

    "give up": [
        "Give up mat karo 💪❤️",
        "Ek baar aur try karo.",
        "Haar ke baad hi jeet ki value samajh aati hai 🔥",
        "Thoda rest lo, phir dobara start karo 💪"
    ],

    # ❓ GENERAL QUESTIONS
    "kya": [
        "Bolo 😊 Kya jaana hai?",
        "Haan, batao kya baat hai?",
        "Kya hua dost? 🤖",
        "Bolo, Nova sun raha hai."
    ],

    "kyun": [
        "Ye interesting question hai 😄",
        "Kyunki kabhi-kabhi aisa ho jata hai 😊",
        "Achha sawaal hai 🤖",
        "Iska jawab situation par depend karta hai."
    ],

    "kaise": [
        "Batao kis cheez ko kaise karna hai? 😊",
        "Main samjhane ki koshish karta hoon 🤖",
        "Thoda detail me bolo dost.",
        "Haan, batao kya karna hai?"
    ],

    # 🗣️ RANDOM CHAT
    "bore": [
        "Bore ho rahe ho? 😄 Chalo baat karte hain.",
        "Ek joke sunaun? 😂",
        "Kuch interesting karte hain 😎",
        "Boredom ko bhagate hain 🤖🔥"
    ],

    "bored": [
        "Bored ho? 😄 Main hoon na!",
        "Chalo kuch interesting baat karte hain.",
        "Ek funny joke sunoge? 😂",
        "Boredom khatam karte hain 😎"
    ],

    "busy": [
        "Achha 😄 Jab free ho tab baat karna.",
        "Theek hai dost ❤️ Kaam pe focus karo.",
        "No problem 😊",
        "Free hoke wapas aana 🤖"
    ],

    # 🙏 NAMASTE
    "namaste": [
        "Namaste 🙏😊 Kaise ho?",
        "Namaste dost 🙏❤️",
        "Namaste ji 😊 Nova aapka swagat karta hai.",
        "🙏 Namaste! Batao kya baat hai?"
    ],

    # 🤔 THINKING
    "soch": [
        "Hmm 🤔 Sochna bhi zaroori hai.",
        "Achha, kya soch rahe ho? 😊",
        "Nova bhi soch raha hai 🤖😂",
        "Batao kya chal raha hai dimaag me?"
    ],
}


def get_random_reply(key: str) -> str:
    """Given keyword/category, return a random fixed reply."""
    replies = REPLIES.get(key, [])
    if not replies:
        return "Bolo dost 😊 Nova sun raha hai."
    return random.choice(replies)
