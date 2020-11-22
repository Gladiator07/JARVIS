from Jarvis import JarvisAssistant
import json, re
obj = JarvisAssistant()


def speak(text):
    obj.tts(text)
while True:
    command = obj.mic_input()

    if re.search('date', command):
        date = obj.tell_me_date()
        print(date)
        speak(date)
    

# def speak(text):
#     obj.tts(text)
# memory = obj.read_json()
# # command = obj.mic_input()


# if re.search('date', command):
#     date = obj.tell_me_date()
#     print(date)
#     speak(date)
