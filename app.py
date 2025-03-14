from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv('GOOGLE_API_KEY')

client = genai.Client(api_key=key)

chat = client.chats.create(model="gemini-2.0-flash")
response = chat.send_message("I have 2 dogs in my house.")

response = chat.send_message("How many paws are in my house?")

for message in chat._curated_history:
    print(f'role - {message.role}', end=": ")
    print(message.parts[0].text)
