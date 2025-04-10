from google import genai

class GeminiChat:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key = api_key)
        self.chat = self.client.chats.create(model="gemini-2.0-flash")
    
    def send_message(self, message):
        response = self.chat.send_message(message)
        return response.text
    
    def get_history(self):
        return [(msg.role, msg.parts[0].text) for msg in self.chat._curated_history]
