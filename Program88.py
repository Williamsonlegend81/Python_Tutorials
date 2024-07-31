import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

ld = ["Harry","Vrund","Ansh","Parva","Meet","Rudra","Het","Virat","Shaival","Dhairya"]

for name in ld:
    text = f"Shoutout to {name}"
    speak.Speak(text)