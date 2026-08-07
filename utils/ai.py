import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_reply(user_message):
    try:
        response = model.generate_content(user_message)
        return response.text
    except Exception as e:
        return f"Error: {e}"
