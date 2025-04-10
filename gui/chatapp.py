import tkinter as tk
from tkinter import scrolledtext
from ai.gemini import GeminiChat

class ChatApp:
    def __init__(self, root, api_key):
        self.root = root
        self.root.title("AI Chatbot")
        self.root.geometry("500x600")
        self.root.configure(bg="#121212")
        
        self.chatbot = GeminiChat(api_key=api_key)
        
        self.title_label = tk.Label(root, text="AI Chatbot", font=("Arial", 16, "bold"), fg="white", bg="#121212")
        self.title_label.pack(pady=10)
        
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, bg="#1E1E1E", fg="white", font=("Arial", 12))
        self.chat_display.pack(padx=10, pady=10)
        self.chat_display.config(state=tk.DISABLED)
        
        self.entry_frame = tk.Frame(root, bg="#121212")
        self.entry_frame.pack(pady=5)
        
        self.entry = tk.Entry(self.entry_frame, width=40, font=("Arial", 12), bg="#1E1E1E", fg="white", insertbackground="white")
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.bind("<Return>", lambda event: self.process_message())
        
        self.send_button = tk.Button(self.entry_frame, text="Send", command=self.process_message, font=("Arial", 12), bg="#0078D7", fg="white")
        self.send_button.pack(side=tk.RIGHT)
        
    def process_message(self):
        user_message = self.entry.get()
        if user_message:
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.insert(tk.END, f"You: {user_message}\n", "user")
            self.chat_display.tag_config("user", foreground="#00FF00")
            
            response = self.chatbot.send_message(user_message)
            self.chat_display.insert(tk.END, f"Chatbot: {response}\n\n", "gemini")
            self.chat_display.tag_config("gemini", foreground="#00BFFF")
            
            self.chat_display.config(state=tk.DISABLED)
            self.entry.delete(0, tk.END)