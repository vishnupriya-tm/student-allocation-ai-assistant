import google.generativeai as genai
from decouple import config

genai.configure(
    api_key=config("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

response = model.generate_content(
    "Say hello in one sentence."
)

print(response.text)

