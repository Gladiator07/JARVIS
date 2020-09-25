## Run this command in terminal  before executing this program
## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also run this in seperate terminal
## rasa run actions

import requests
import speech_recognition as sr     # import the library
# import subprocess
import pyttsx3

# from gtts import gTTS

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# rate = engine.getProperty('rate')


def speak(text):
    engine.say(text)
    engine.runAndWait()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 180)


# sender = input("What is your name?\n")

bot_message = ""
message=""

r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})

print("Bot says, ",end=' ')
for i in r.json():
    bot_message = i['text']
    print(f"{bot_message}")

speak(bot_message)
# myobj = gTTS(text=bot_message)
# myobj.save("welcome.mp3")
# print('saved')
# Playing the converted file
# subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])


# Function for recognizing the voice and converting it into text
def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

        r.adjust_for_ambient_noise(sour, duration=1)

        audio = r.listen(source)

        try:
            print("Recognizing")
            command = r.recognize_google(audio, language='en-in')
            print(f"You said: {command}\n")

        except:
            speak("Please try saying again")

            return "None"
    return command


while bot_message != "Bye" or bot_message!='thanks':

    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            message = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
            print("You said : {}".format(message))

        except:
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
    if len(message)==0:
        continue
    print("Sending message now...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    print("Bot says, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    speak(bot_message)
#     myobj = gTTS(text=bot_message)
#     myobj.save("welcome.mp3")
#     print('saved')
#     # Playing the converted file
#     subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])

if __name__ == "__main__":
    #start()
    while True:
        command = myCommand()