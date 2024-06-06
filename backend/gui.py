import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import webbrowser
import threading
import subprocess

def run_flask():
    subprocess.run(["flask", "run"])

def open_browser():
    webbrowser.open('http://localhost:5000')

def start_server():
    threading.Thread(target=run_flask).start()
    threading.Timer(1.0, open_browser).start()

app = tk.Tk()
app.title('AI Chatbot')
app.geometry('800x600')

label = ttk.Label(app, text="AI Chatbot", font=("Helvetica", 18))
label.pack(pady=20)

start_button = ttk.Button(app, text="Start Server and Open App", command=start_server)
start_button.pack(pady=20)

app.mainloop()
