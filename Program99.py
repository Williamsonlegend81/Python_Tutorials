import winsound
import win32com.client as wincom
import time

speak = wincom.Dispatch("SAPI.SpVoice")

while True:
    t = time.time()
    time.sleep(3600)
    frequency = 2500
    duration = 1000
    winsound.Beep(frequency,duration)
    speak.Speak("Drink water!")