import tkinter as tk
from dotenv import load_dotenv
from gui.chatapp import ChatApp
import os

# Load environment variables
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root, api_key)
    root.mainloop()
