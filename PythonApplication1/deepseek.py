import tkinter as tk
from tkinter import scrolledtext, END
from openai import OpenAI

class deepseek:
    def __init__(self, root):
        self.root = root
        self.root.title("DeepSeek Chat")

        self.chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
        self.chat_window.pack(padx=10, pady=10)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(padx=10, pady=(0, 10))
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=(0, 10))

    def send_message(self, event=None):
        message = self.entry.get()
        if message:
            self.chat_window.insert(END, "You: " + message + '\n')
            self.entry.delete(0, END)
            response = self.get_response_from_api(message)
            self.chat_window.insert(END, "Bot: " + response + '\n')

    def get_response_from_api(self, user_message):
        try:
            client = OpenAI(api_key="sk-916adfb87fc84389bb813900309ba1c5", base_url="https://api.deepseek.com")

            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant"},
                    {"role": "user", "content": user_message},
                ],
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def open_chat_window():
        chat_window = tk.Toplevel()
        app = deepseek(chat_window)
        chat_window.mainloop()
