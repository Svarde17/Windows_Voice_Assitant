# import customtkinter as ctk
# from tkinter import scrolledtext, PhotoImage
# import pyttsx3
# import speech_recognition as sr
# import datetime
# import wikipedia
# import webbrowser
# import os
# import smtplib
# import threading
# import time
# import pyautogui
# import subprocess
# import pywhatkit
# import requests
# import json
# import psutil

# # Initial Configuration
# GEMINI_API_KEY = "AIzaSyBnY8p5TfDaypstAsOTZGqaYy7vVKcwjZA"
# EMAIL_ADDRESS = 'your-email@gmail.com'
# EMAIL_PASSWORD = 'your-app-password'
# CODE_PATH = r"C:\\Users\\sahil\\OneDrive\\Desktop\\VA\\Code.exe"

# # Voice Setup
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

# # State
# chat_history = []
# is_muted = False
# is_listening = True

# # Functions
# def speak(audio):
#     if not is_muted:
#         engine.say(audio)
#         engine.runAndWait()

# def stop_speaking():
#     engine.stop()

# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     greeting = "Good Morning!" if hour < 12 else "Good Afternoon!" if hour < 18 else "Good Evening!"
#     speak(greeting)
#     speak("I am your smart assistant, ready to help you.")

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1.2
#         audio = r.listen(source, timeout=5, phrase_time_limit=10)
#     try:
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")
#         return query.lower()
#     except sr.UnknownValueError:
#         return "None"

# def askGemini(prompt):
#     url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-pro:generateContent?key={GEMINI_API_KEY}"
#     headers = {"Content-Type": "application/json"}
#     data = {"contents": [{"parts": [{"text": prompt}]}]}
#     try:
#         response = requests.post(url, headers=headers, json=data)
#         return response.json()['candidates'][0]['content']['parts'][0]['text']
#     except:
#         return "I couldn't fetch a valid response from Gemini."

# def update_chatbox():
#     chatbox.configure(state="normal")
#     chatbox.delete("1.0", "end")
#     for msg in chat_history[-30:]:
#         chatbox.insert("end", msg + "\n\n")
#     chatbox.configure(state="disabled")
#     chatbox.see("end")

# def handleQuery(query):
#     global is_muted, is_listening
#     chat_history.append(f"🧑 You: {query}")

#     if 'stop speaking' in query or 'stop assistant' in query:
#         is_listening = False
#         stop_speaking()
#         chat_history.append("🤖 Assistant: Stopped speaking.")
#         speak("Assistant stopped. Say 'start assistant' to resume.")
#         update_chatbox()
#         return

#     if 'start assistant' in query:
#         is_listening = True
#         speak("Voice re-enabled.")
#         chat_history.append("🤖 Assistant: Voice re-enabled.")
#         update_chatbox()
#         return

#     if 'mute' in query:
#         is_muted = True
#         chat_history.append("🤖 Assistant: Muted.")
#         return
#     if 'unmute' in query:
#         is_muted = False
#         speak("Unmuted")
#         chat_history.append("🤖 Assistant: Unmuted.")
#         return

#     if 'battery' in query:
#         battery = psutil.sensors_battery()
#         plugged = "Charging" if battery.power_plugged else "Not Charging"
#         response = f"Battery is at {battery.percent}% and is {plugged}."
#         speak(response)
#         chat_history.append(f"🤖 Assistant: {response}")

#     elif 'open terminal' in query:
#         subprocess.Popen('cmd.exe')
#         chat_history.append("🤖 Assistant: Opened Terminal")

#     elif 'create file' in query:
#         speak("What should I name the file?")
#         filename = takeCommand().replace(" ", "_") + ".txt"
#         with open(filename, "w") as f:
#             f.write("Created by your Assistant")
#         os.startfile(filename)
#         chat_history.append(f"🤖 Assistant: Created file {filename}")

#     elif 'wikipedia' in query:
#         results = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)
#         speak(results)
#         chat_history.append(f"🤖 Assistant: {results}")

#     elif 'open youtube' in query:
#         webbrowser.open("https://youtube.com")

#     elif 'open google' in query:
#         webbrowser.open("https://google.com")

#     elif 'open chrome' in query:
#         chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
#         subprocess.Popen(chrome_path)

#     elif 'open folder' in query:
#         folder_name = query.replace("open folder", "").strip()
#         os.system(f'explorer {folder_name}')

#     elif 'search for' in query:
#         search_term = query.split("search for")[-1].strip()
#         webbrowser.open(f"https://www.google.com/search?q={search_term}")

#     elif 'trending mobiles' in query:
#         webbrowser.open("https://www.amazon.in/s?k=trending+mobiles")

#     elif 'play music' in query:
#         speak("Which song?")
#         song = takeCommand()
#         pywhatkit.playonyt(song)

#     elif 'shutdown pc' in query:
#         speak("Shutting down.")
#         os.system("shutdown /s /t 1")

#     elif 'restart pc' in query:
#         speak("Restarting.")
#         os.system("shutdown /r /t 1")

#     elif 'open' in query:
#         apps = {
#             'notepad': 'notepad.exe',
#             'calculator': 'calc.exe',
#             'paint': 'mspaint.exe',
#             'excel': ['start', 'excel'],
#             'word': ['start', 'winword']
#         }
#         for name, path in apps.items():
#             if name in query:
#                 subprocess.Popen(path, shell=True if isinstance(path, list) else False)
#                 chat_history.append(f"🤖 Assistant: Opening {name.capitalize()}")
#                 break

#     elif 'volume up' in query:
#         pyautogui.press("volumeup")
#     elif 'volume down' in query:
#         pyautogui.press("volumedown")
#     elif 'mute' in query:
#         pyautogui.press("volumemute")

#     elif 'bye' in query:
#         speak("Goodbye! Have a nice day.")
#         os._exit(0)

#     else:
#         speak("Let me check.")
#         reply = askGemini(query)
#         speak(reply)
#         chat_history.append(f"🤖 Assistant: {reply}")

#     update_chatbox()

# # Assistant Loop
# def assistant_loop():
#     wishMe()
#     while True:
#         if is_listening:
#             query = takeCommand()
#             if query and query != "None":
#                 handleQuery(query)
#                 if is_listening:
#                     speak("Next command?")
#         else:
#             time.sleep(1)

# # Launch GUI
# def launch_gui():
#     global chatbox

#     ctk.set_appearance_mode("dark")
#     ctk.set_default_color_theme("blue")

#     root = ctk.CTk()
#     root.title("🧠 Smart Assistant")
#     root.geometry("1100x700")

#     sidebar = ctk.CTkFrame(master=root, width=260, corner_radius=0)
#     sidebar.pack(side="left", fill="y")

#     logo = ctk.CTkLabel(master=sidebar, text="🤖 Smart Assistant", font=("Times New Roman", 24, "bold"))
#     logo.pack(pady=(30, 10))

#     ctk.CTkLabel(master=sidebar, text="Status: Listening", font=("Times New Roman", 14)).pack(pady=(5, 10))

#     ctk.CTkButton(master=sidebar, text="Mute", command=lambda: handleQuery("mute"), font=("Times New Roman", 14)).pack(pady=4)
#     ctk.CTkButton(master=sidebar, text="Unmute", command=lambda: handleQuery("unmute"), font=("Times New Roman", 14)).pack(pady=4)
#     ctk.CTkButton(master=sidebar, text="Stop Assistant", command=lambda: handleQuery("stop assistant"), font=("Times New Roman", 14)).pack(pady=4)
   
#     ctk.CTkButton(master=sidebar, text="Battery Status", command=lambda: handleQuery("battery"), font=("Times New Roman", 14)).pack(pady=4)
#     ctk.CTkButton(master=sidebar, text="Exit", command=root.destroy, fg_color="#dc3545", hover_color="#c82333", font=("Times New Roman", 14)).pack(pady=20)

#     ctk.CTkLabel(master=sidebar, text="Made by Sahil Varde", font=("Times New Roman", 12)).pack(side="bottom", pady=10)

#     main_frame = ctk.CTkFrame(master=root)
#     main_frame.pack(padx=20, pady=20, fill="both", expand=True)

#     image_frame = ctk.CTkFrame(master=main_frame)
#     image_frame.pack(fill="x", pady=(0, 10))

    

#     chat_frame = ctk.CTkFrame(master=main_frame, fg_color="#f8f9fa", corner_radius=10)
#     chat_frame.pack(fill="both", expand=True)

#     chatbox = scrolledtext.ScrolledText(master=chat_frame, wrap="word", font=("Times New Roman", 13), bg="#ffffff", fg="#000000")
#     chatbox.pack(fill="both", expand=True)
#     chatbox.configure(state="disabled")

#     threading.Thread(target=assistant_loop, daemon=True).start()
#     root.mainloop()

# if __name__ == "__main__":
#     launch_gui()


# import customtkinter as ctk
# from tkinter import scrolledtext
# import pyttsx3
# import speech_recognition as sr
# import datetime
# import wikipedia
# import webbrowser
# import os
# import smtplib
# import threading
# import time
# import pyautogui
# import subprocess
# import pywhatkit
# import requests
# import json
# import psutil

# # ------------------- CONFIG ------------------- #
# GEMINI_API_KEY = "AIzaSyCfRj_8szqjSS3G9sleUOXw8D40JFjDk0k"
# EMAIL_ADDRESS = 'your-email@gmail.com'
# EMAIL_PASSWORD = 'your-app-password'

# # ------------------- INITIAL SETUP ------------------- #
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

# chat_history = []
# is_muted = False
# is_listening = True

# # ------------------- FUNCTIONS ------------------- #
# def speak(audio):
#     if not is_muted:
#         engine.say(audio)
#         engine.runAndWait()

# def stop_speaking():
#     engine.stop()

# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     greeting = "Good Morning!" if hour < 12 else "Good Afternoon!" if hour < 18 else "Good Evening!"
#     speak(greeting)
#     speak("I am your smart assistant, ready to help you.")

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1.2
#         audio = r.listen(source, timeout=5, phrase_time_limit=10)
#     try:
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")
#         return query.lower()
#     except sr.UnknownValueError:
#         return "None"
#     except sr.RequestError:
#         return "None"

# def askGemini(prompt):
#     url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
#     headers = {"Content-Type": "application/json"}
#     data = {"contents": [{"parts": [{"text": prompt}]}]}
#     try:
#         response = requests.post(url, headers=headers, json=data)
#         if response.status_code == 200:
#             return response.json()['candidates'][0]['content']['parts'][0]['text']
#         else:
#             return "Gemini API Error: " + response.reason
#     except Exception as e:
#         return f"Error: {str(e)}"

# def update_chatbox():
#     chatbox.configure(state="normal")
#     chatbox.delete("1.0", "end")
#     for msg in chat_history[-30:]:
#         chatbox.insert("end", msg + "\n\n")
#     chatbox.configure(state="disabled")
#     chatbox.see("end")

# def handleQuery(query):
#     global is_muted, is_listening
#     chat_history.append(f"🧑 You: {query}")

#     if 'stop speaking' in query or 'stop assistant' in query:
#         is_listening = False
#         stop_speaking()
#         chat_history.append("🤖 Assistant: Stopped speaking.")
#         speak("Assistant stopped. Say 'start assistant' to resume.")
#         update_chatbox()
#         return

#     if 'start assistant' in query:
#         is_listening = True
#         speak("Voice re-enabled.")
#         chat_history.append("🤖 Assistant: Voice re-enabled.")
#         update_chatbox()
#         return

#     if 'mute' in query:
#         is_muted = True
#         chat_history.append("🤖 Assistant: Muted.")
#         return
#     if 'unmute' in query:
#         is_muted = False
#         speak("Unmuted")
#         chat_history.append("🤖 Assistant: Unmuted.")
#         return

#     if 'battery' in query:
#         battery = psutil.sensors_battery()
#         plugged = "Charging" if battery.power_plugged else "Not Charging"
#         response = f"Battery is at {battery.percent}% and is {plugged}."
#         speak(response)
#         chat_history.append(f"🤖 Assistant: {response}")

#     elif 'open terminal' in query:
#         subprocess.Popen('cmd.exe')
#         chat_history.append("🤖 Assistant: Opened Terminal")

#     elif 'create file' in query:
#         speak("What should I name the file?")
#         filename = takeCommand().replace(" ", "_") + ".txt"
#         with open(filename, "w") as f:
#             f.write("Created by your Assistant")
#         os.startfile(filename)
#         chat_history.append(f"🤖 Assistant: Created file {filename}")

#     elif 'wikipedia' in query:
#         results = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)
#         speak(results)
#         chat_history.append(f"🤖 Assistant: {results}")

#     elif 'open youtube' in query:
#         webbrowser.open("https://youtube.com")

#     elif 'open google' in query:
#         webbrowser.open("https://google.com")

#     elif 'open chrome' in query:
#         chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
#         subprocess.Popen(chrome_path)
    
#     elif 'thank you' in query:
#         speak("You're welcome!")
#         chat_history.append("🤖 Assistant: You're welcome!")
#         return
    
#     elif 'chatgpt' in query:
#         webbrowser.open("https://chat.openai.com")
#         speak("Opening ChatGPT")
#         return
#     elif 'open my github' in query:
#         webbrowser.open("https://github.com/your-github-profile")  # customize this
#         speak("Opening your GitHub")
#         return

#     elif 'open folder' in query:
#         folder_name = query.replace("open folder", "").strip()
#         os.system(f'explorer {folder_name}')

#     elif 'search for' in query:
#         search_term = query.split("search for")[-1].strip()
#         webbrowser.open(f"https://www.google.com/search?q={search_term}")

#     elif 'trending mobiles' in query:
#         webbrowser.open("https://www.amazon.in/s?k=trending+mobiles")

#     elif 'play music' in query:
#         speak("Which song?")
#         song = takeCommand()
#         pywhatkit.playonyt(song)

#     elif 'shutdown pc' in query:
#         speak("Shutting down.")
#         os.system("shutdown /s /t 1")

#     elif 'restart pc' in query:
#         speak("Restarting.")
#         os.system("shutdown /r /t 1")

#     elif 'open' in query:
#         apps = {
#             'notepad': 'notepad.exe',
#             'calculator': 'calc.exe',
#             'paint': 'mspaint.exe',
#             'excel': ['start', 'excel'],
#             'word': ['start', 'winword']
#         }
#         for name, path in apps.items():
#             if name in query:
#                 subprocess.Popen(path, shell=True if isinstance(path, list) else False)
#                 chat_history.append(f"🤖 Assistant: Opening {name.capitalize()}")
#                 break

#     elif 'volume up' in query:
#         pyautogui.press("volumeup")
#     elif 'volume down' in query:
#         pyautogui.press("volumedown")
#     elif 'mute' in query:
#         pyautogui.press("volumemute")

#     elif 'bye' in query:
#         speak("Goodbye! Have a nice day.")
#         os._exit(0)

#     else:
#         speak("Let me check.")
#         reply = askGemini(query)
#         speak(reply)
#         chat_history.append(f"🤖 Assistant: {reply}")

#     update_chatbox()

# def assistant_loop():
#     wishMe()
#     while True:
#         if is_listening:
#             query = takeCommand()
#             if query and query != "None":
#                 handleQuery(query)
#                 if is_listening:
#                     speak("How else may I assist you?")
#         else:
#             time.sleep(1)

# def launch_gui():
#     global chatbox

#     ctk.set_appearance_mode("dark")
#     ctk.set_default_color_theme("blue")

#     root = ctk.CTk()
#     root.title("🧠 Smart Assistant")
#     root.geometry("1100x700")

#     sidebar = ctk.CTkFrame(master=root, width=260, corner_radius=0)
#     sidebar.pack(side="left", fill="y")

#     logo = ctk.CTkLabel(master=sidebar, text="🤖 Smart Assistant", font=("Times New Roman", 24, "bold"))
#     logo.pack(pady=(30, 10))

#     ctk.CTkLabel(master=sidebar, text="Status: Listening", font=("Times New Roman", 14)).pack(pady=(5, 10))
#     ctk.CTkButton(master=sidebar, text="Mute", command=lambda: handleQuery("mute"), font=("Times New Roman", 14)).pack(pady=4)
#     ctk.CTkButton(master=sidebar, text="Unmute", command=lambda: handleQuery("unmute"), font=("Times New Roman", 14)).pack(pady=4)
#     ctk.CTkButton(master=sidebar, text="Stop Assistant", command=lambda: handleQuery("stop assistant"), font=("Times New Roman", 14)).pack(pady=4)
#     ctk.CTkButton(master=sidebar, text="Battery Status", command=lambda: handleQuery("battery"), font=("Times New Roman", 14)).pack(pady=4)
#     ctk.CTkButton(master=sidebar, text="Exit", command=root.destroy, fg_color="#dc3545", hover_color="#c82333", font=("Times New Roman", 14)).pack(pady=20)
#     ctk.CTkLabel(master=sidebar, text="Made by Sahil Varde", font=("Times New Roman", 12)).pack(side="bottom", pady=10)

#     main_frame = ctk.CTkFrame(master=root)
#     main_frame.pack(padx=20, pady=10, fill="both", expand=True)

#     chat_frame = ctk.CTkFrame(master=main_frame, fg_color="#f8f9fa", corner_radius=10)
#     chat_frame.pack(fill="both", expand=True)

#     chatbox = scrolledtext.ScrolledText(master=chat_frame, wrap="word", font=("Times New Roman", 13), bg="#ffffff", fg="#000000")
#     chatbox.pack(fill="both", expand=True)
#     chatbox.configure(state="disabled")

#     threading.Thread(target=assistant_loop, daemon=True).start()
#     root.mainloop()

# if __name__ == "__main__":
#     launch_gui()


import customtkinter as ctk
from tkinter import scrolledtext
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import threading
import time
import pyautogui
import subprocess
import pywhatkit
import requests
import json
import psutil
import traceback

# ------------------- CONFIG ------------------- #
GEMINI_API_KEY = "AIzaSyCfRj_8szqjSS3G9sleUOXw8D40JFjDk0k"
EMAIL_ADDRESS = 'your-email@gmail.com'
EMAIL_PASSWORD = 'your-app-password'

# ------------------- INITIAL SETUP ------------------- #
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

chat_history = []
is_muted = False
is_listening = True
chatbox = None  # Will be set inside GUI

# ------------------- FUNCTIONS ------------------- #
def speak(audio):
    if not is_muted:
        engine.say(audio)
        engine.runAndWait()

def stop_speaking():
    engine.stop()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    greeting = "Good Morning!" if hour < 12 else "Good Afternoon!" if hour < 18 else "Good Evening!"
    speak(greeting)
    speak("I am your smart assistant, ready to help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.0
        r.energy_threshold = 300
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            return "None"
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except (sr.UnknownValueError, sr.RequestError):
        return "None"

def askGemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        else:
            return "Gemini API Error: " + response.reason
    except Exception as e:
        return f"Error: {str(e)}"

def update_chatbox():
    if chatbox:
        chatbox.configure(state="normal")
        chatbox.delete("1.0", "end")
        for msg in chat_history[-30:]:
            chatbox.insert("end", msg + "\n\n")
        chatbox.configure(state="disabled")
        chatbox.see("end")

def handleQuery(query):
    global is_muted, is_listening
    try:
        if not query or query == "None":
            return

        chat_history.append(f"🧑 You: {query}")

        if 'stop speaking' in query or 'stop assistant' in query:
            is_listening = False
            stop_speaking()
            chat_history.append("🤖 Assistant: Stopped speaking.")
            speak("Assistant stopped. Say 'start assistant' to resume.")
            update_chatbox()
            return

        if 'start assistant' in query:
            is_listening = True
            speak("Voice re-enabled.")
            chat_history.append("🤖 Assistant: Voice re-enabled.")
            update_chatbox()
            return

        if 'mute' in query:
            is_muted = True
            chat_history.append("🤖 Assistant: Muted.")
            update_chatbox()
            return

        if 'unmute' in query:
            is_muted = False
            speak("Unmuted")
            chat_history.append("🤖 Assistant: Unmuted.")
            update_chatbox()
            return

        if 'battery' in query:
            battery = psutil.sensors_battery()
            if battery:
                plugged = "Charging" if battery.power_plugged else "Not Charging"
                response = f"Battery is at {battery.percent}% and is {plugged}."
                speak(response)
                chat_history.append(f"🤖 Assistant: {response}")
            else:
                chat_history.append("🤖 Assistant: Battery status unavailable.")

        elif 'open terminal' in query:
            subprocess.Popen('start cmd', shell=True)
            chat_history.append("🤖 Assistant: Opened Terminal")

        elif 'create file' in query:
            speak("What should I name the file?")
            filename = takeCommand()
            if filename and filename != "None":
                filename = filename.replace(" ", "_") + ".txt"
                with open(filename, "w") as f:
                    f.write("Created by your Assistant")
                os.startfile(filename)
                chat_history.append(f"🤖 Assistant: Created file {filename}")
            else:
                speak("File creation cancelled.")

        elif 'wikipedia' in query:
            topic = query.replace("wikipedia", "").strip()
            results = wikipedia.summary(topic, sentences=2)
            speak(results)
            chat_history.append(f"🤖 Assistant: {results}")

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open chrome' in query:
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
            if os.path.exists(chrome_path):
                subprocess.Popen(chrome_path)
            else:
                speak("Chrome not found.")

        elif 'thank you' in query:
            speak("You're welcome!")
            chat_history.append("🤖 Assistant: You're welcome!")

        elif 'chatgpt' in query:
            webbrowser.open("https://chat.openai.com")
            speak("Opening ChatGPT")

        elif 'open my github' in query:
            webbrowser.open("https://github.com/your-github-profile")
            speak("Opening your GitHub")

        elif 'open folder' in query:
            folder_name = query.replace("open folder", "").strip()
            os.system(f'explorer "{folder_name}"')

        elif 'search for' in query:
            search_term = query.split("search for")[-1].strip()
            webbrowser.open(f"https://www.google.com/search?q={search_term}")

        elif 'trending mobiles' in query:
            webbrowser.open("https://www.amazon.in/s?k=trending+mobiles")

        elif 'play music' in query:
            speak("Which song?")
            song = takeCommand()
            if song and song != "None":
                pywhatkit.playonyt(song)

        elif 'shutdown pc' in query:
            speak("Shutting down.")
            os.system("shutdown /s /t 1")

        elif 'restart pc' in query:
            speak("Restarting.")
            os.system("shutdown /r /t 1")

        elif 'open' in query:
            apps = {
                'notepad': 'notepad.exe',
                'calculator': 'calc.exe',
                'paint': 'mspaint.exe',
                'excel': ['start', 'excel'],
                'word': ['start', 'winword']
            }
            for name, path in apps.items():
                if name in query:
                    subprocess.Popen(path, shell=True if isinstance(path, list) else False)
                    chat_history.append(f"🤖 Assistant: Opening {name.capitalize()}")
                    break

        elif 'volume up' in query:
            pyautogui.press("volumeup")
        elif 'volume down' in query:
            pyautogui.press("volumedown")
        elif 'mute' in query:
            pyautogui.press("volumemute")

        elif 'bye' in query:
            speak("Goodbye! Have a nice day.")
            os._exit(0)

        else:
            speak("Let me check.")
            reply = askGemini(query)
            speak(reply)
            chat_history.append(f"🤖 Assistant: {reply}")

        update_chatbox()

    except Exception as e:
        chat_history.append(f"🤖 Assistant Error: {str(e)}")
        traceback.print_exc()
        update_chatbox()

def assistant_loop():
    wishMe()
    while True:
        if is_listening:
            query = takeCommand()
            if query and query != "None":
                handleQuery(query)
                if is_listening:
                    speak("How else may I assist you?")
        else:
            time.sleep(1)

def launch_gui():
    global chatbox

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("🧠 Smart Assistant")
    root.geometry("1100x700")

    sidebar = ctk.CTkFrame(master=root, width=260, corner_radius=0)
    sidebar.pack(side="left", fill="y")

    logo = ctk.CTkLabel(master=sidebar, text="🤖 Voice Assistant", font=("Times New Roman", 24, "bold"))
    logo.pack(pady=(30, 10))

    ctk.CTkLabel(master=sidebar, text="Status: Listening", font=("Times New Roman", 14)).pack(pady=(5, 10))
    # ctk.CTkButton(master=sidebar, text="Mute", command=lambda: handleQuery("mute"), font=("Times New Roman", 14)).pack(pady=4)
    # ctk.CTkButton(master=sidebar, text="Unmute", command=lambda: handleQuery("unmute"), font=("Times New Roman", 14)).pack(pady=4)
    ctk.CTkButton(master=sidebar, text="Stop Assistant", command=lambda: handleQuery("stop assistant"), font=("Times New Roman", 14)).pack(pady=4)
    ctk.CTkButton(master=sidebar, text="Battery Status", command=lambda: handleQuery("battery"), font=("Times New Roman", 14)).pack(pady=4)
    ctk.CTkButton(master=sidebar, text="Exit", command=root.destroy, fg_color="#dc3545", hover_color="#c82333", font=("Times New Roman", 14)).pack(pady=20)
    ctk.CTkLabel(master=sidebar, text="Made by Prathmesh", font=("Times New Roman", 12)).pack(side="bottom", pady=10)

    main_frame = ctk.CTkFrame(master=root)
    main_frame.pack(padx=20, pady=10, fill="both", expand=True)

    chat_frame = ctk.CTkFrame(master=main_frame, fg_color="#f8f9fa", corner_radius=10)
    chat_frame.pack(fill="both", expand=True)

    chatbox = scrolledtext.ScrolledText(master=chat_frame, wrap="word", font=("Times New Roman", 13), bg="#ffffff", fg="#000000")
    chatbox.pack(fill="both", expand=True)
    chatbox.configure(state="disabled")

    threading.Thread(target=assistant_loop, daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    launch_gui()
