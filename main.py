from Jarvis import JarvisAssistant
import json, re
obj = JarvisAssistant()


while True:
    command = obj.mic_input()
    

def speak(text):
    obj.tts(text)
memory = obj.read_json()
# command = obj.mic_input()


if re.search('date', command):
    date = obj.tell_me_date()
    print(date)
    speak(date)
