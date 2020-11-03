import pyttsx3
engine = pyttsx3.init()

try:
    engine = pyttsx3.init()
except Exception as e:
    print(e)
voices = engine.getProperty('voices')
print(voices)
for voice in voices:
    print(voice.id)