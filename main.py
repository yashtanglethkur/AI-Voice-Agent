import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import scrolledtext
import datetime

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

# ------------------ SPEAK FUNCTION ------------------
def speak(text):
    engine.stop()
    engine.say(text)
    engine.runAndWait()

# ------------------ LISTEN FUNCTION ------------------
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        update_chat("Listening...\n")
        try:
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
            text = recognizer.recognize_google(audio)
            update_chat(f"You: {text}\n")
            return text.lower()
        except Exception as e:
            update_chat("Could not understand\n")
            return ""

# ------------------ BOT LOGIC ------------------
def get_response(user_input):
    if "Hello" in user_input:
        return "Hello! Welcome to Ascent Media. How can I assist you today?"

    elif "accent media" in user_input:
        return "Ascent Media is a digital solutions company. Say how can i help you with the Services! Yash Sirr  "

    elif "Services" in user_input:
        return "We offer web development, digital marketing, and AI solutions."

    elif "Time" in user_input:
        return "Current time is " + datetime.datetime.now().strftime("%H:%M")

    elif "Bye" in user_input or "exit" in user_input:
        return "Goodbye!"

    else:
        return "Sorry, I didn't understand that."

# ------------------ CHAT UPDATE ------------------
def update_chat(message):
    chat_area.insert(tk.END, message)
    chat_area.yview(tk.END)

# ------------------ BUTTON ACTIONS ------------------
def send_text():
    user_input = entry.get()
    entry.delete(0, tk.END)

    if user_input == "":
        return

    update_chat(f"You: {user_input}\n")
    response = get_response(user_input.lower())

    update_chat(f"AI: {response}\n")
    speak(response)

def use_mic():
    user_input = listen()

    if user_input == "":
        return

    response = get_response(user_input)
    update_chat(f"AI: {response}\n")
    speak(response)

# ------------------ GUI SETUP ------------------
root = tk.Tk()
root.title("AI Voice Agent")
root.geometry("500x600")

# Chat display
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Input field
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(padx=10, pady=5, fill=tk.X)

# Buttons
frame = tk.Frame(root)
frame.pack(pady=10)

send_btn = tk.Button(frame, text="Send", command=send_text, width=10)
send_btn.grid(row=0, column=0, padx=5)

mic_btn = tk.Button(frame, text="🎤 Speak", command=use_mic, width=10)
mic_btn.grid(row=0, column=1, padx=5)

# Start GUI
update_chat("AI Voice Agent Started (GUI Mode)\n")
root.mainloop()