import os
import tkinter as tk
from tkinter import scrolledtext
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GeminiChat:
    def __init__(self):
        self.api_key = os.getenv('GOOGLE_API_KEY')
        self.client = genai.Client(api_key=self.api_key)
        self.chat = self.client.chats.create(model="gemini-2.0-flash")
    
    def send_message(self, message):
        response = self.chat.send_message(message)
        return response.text
    
    def get_history(self):
        return [(msg.role, msg.parts[0].text) for msg in self.chat._curated_history]

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gemini AI Chatbot")
        self.root.geometry("500x600")
        self.root.configure(bg="#121212")
        
        self.chatbot = GeminiChat()
        
        self.title_label = tk.Label(root, text="Gemini AI Chatbot", font=("Arial", 16, "bold"), fg="white", bg="#121212")
        self.title_label.pack(pady=10)
        
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, bg="#1E1E1E", fg="white", font=("Arial", 12))
        self.chat_display.pack(padx=10, pady=10)
        self.chat_display.config(state=tk.DISABLED)
        
        self.entry_frame = tk.Frame(root, bg="#121212")
        self.entry_frame.pack(pady=5)
        
        self.entry = tk.Entry(self.entry_frame, width=40, font=("Arial", 12), bg="#1E1E1E", fg="white", insertbackground="white")
        self.entry.pack(side=tk.LEFT, padx=5)
        
        self.send_button = tk.Button(self.entry_frame, text="Send", command=self.process_message, font=("Arial", 12), bg="#0078D7", fg="white")
        self.send_button.pack(side=tk.RIGHT)
        
    def process_message(self):
        user_message = self.entry.get()
        if user_message:
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.insert(tk.END, f"You: {user_message}\n", "user")
            self.chat_display.tag_config("user", foreground="#00FF00")
            
            response = self.chatbot.send_message(user_message)
            self.chat_display.insert(tk.END, f"Gemini: {response}\n\n", "gemini")
            self.chat_display.tag_config("gemini", foreground="#00BFFF")
            
            self.chat_display.config(state=tk.DISABLED)
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
