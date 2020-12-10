from Jarvis import JarvisAssistant
import json
import re
import random
import pprint
import webbrowser
import config
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request  # used to make requests
import urllib.parse  # used to parse values into the url
import pyjokes
import time
obj = JarvisAssistant()

# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
             "ok jarvis", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

EMAIL_DIC = {
    'myself': 'atharvaaingle@gmail.com',
    'my official email': 'atharvaaingle@gmail.com',
    'my second email': 'atharvaaingle@gmail.com',
    'my official mail': 'atharvaaingle@gmail.com',
    'my second mail': 'atharvaaingle@gmail.com'
}

CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]
# =======================================================================================================================================================
def speak(text):
    obj.tts(text)


while True:
    command = obj.mic_input()

    if re.search('date', command):
        date = obj.tell_me_date()
        print(date)
        speak(date)

    if "time" in command:
        time = obj.tell_time()
        print(time)
        speak(f"Sir the time is {time}")

    if re.search('launch', command):
        dict_app = {
            'chrome': 'C:/Program Files/Google/Chrome/Application/chrome'
        }

        app = command.split(' ', 1)[1]
        path = dict_app.get(app)

        if path is None:
            speak('Application path not found')
            print('Application path not found')

        else:
            speak('Launching: ' + app + 'for you sir!')
            obj.launch_any_app(path_of_app=path)

    if command in GREETINGS:
        speak(random.choice(GREETINGS_RES))

    if re.search('open', command):
        domain = command.split(' ')[-1]
        open_result = obj.website_opener(domain)
        speak(f'Alright sir !! Opening {domain}')
        print(open_result)

    if re.search('weather', command):
        city = command.split(' ')[-1]
        weather_res = obj.weather(city=city)
        print(weather_res)
        speak(weather_res)

    if re.search('tell me about', command):
        topic = command.split(' ')[-1]
        if topic:
            wiki_res = obj.tell_me(topic)
            print(wiki_res)
            speak(wiki_res)
        else:
            speak(
                "Sorry sir. I couldn't load your query from my database. Please try again")

    if "buzzing" in command or "news" in command or "headlines" in command:
        news_res = obj.news()
        speak('Source: The Times Of India')
        speak('Todays Headlines are..')
        for index, articles in enumerate(news_res):
            pprint.pprint(articles['title'])
            speak(articles['title'])
            if index == len(news_res)-1:
                break
            # speak('Moving on the next news headline..')
        speak('These were the top headlines, Have a nice day Sir!!..')

    if 'search google for' in command:
        obj.search_anything_google(command)
        

    # elif 'youtube' in command:
    #     speak('Ok!')
    #     reg_ex = re.search('youtube (.+)', command)
    #     if reg_ex:
    #         domain = command.split("youtube",1)[1]
    #         song = urllib.parse.urlencode({"search_query" : domain})
    #         print(song)

    #         # fetch the ?v=query_string
    #         result = urllib.request.urlopen("http://www.youtube.com/results?" + song)
    #         print(result)

    #         # make the url of the first result song
    #         search_results = re.findall(r'href=\"\/watch\?v=(.{11})', result.read().decode())
    #         print(search_results)

    #         # make the final url of song selects the very first result from youtube result
    #         url = "http://www.youtube.com/watch?v="+search_results[0]

    #         # play the song using webBrowser module which opens the browser 
    #         # webbrowser.open(url, new = 1)
    #         webbrowser.open_new(url)

    if "email" in command or "send email" in command:
        sender_email = config.email
        sender_password = config.email_password

        try:
            speak("Whom do you want to email sir ?")
            recipient = obj.mic_input()
            receiver_email = EMAIL_DIC.get(recipient)
            if receiver_email:

                speak("What is the subject sir ?")
                subject = obj.mic_input()
                speak("What should I say?")
                message = obj.mic_input()
                msg = 'Subject: {}\n\n{}'.format(subject, message)
                obj.send_mail(sender_email, sender_password,
                              receiver_email, msg)
                speak("Email has been successfully sent")

            else:
                speak(
                    "I coudn't find the requested person's email in my database. Please try again with a different name")

        except:
            speak("Sorry sir. Couldn't send your mail. Please try again")

    elif "what do i have" in command or "do i have plans" or "am i busy" in command:
        obj.google_calendar_events(command)

    if "make a note" in command or "write this down" in command or "remember this" in command:
        speak("What would you like me to write down?")
        note_text = obj.mic_input()
        obj.take_note(note_text)
        speak("I've made a note of that")
    
    if "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
    
    if "system" in command:
        sys_info = obj.system_info()
        print(sys_info)
        speak(sys_info)
    
    if "where is" in command:
        place = command.split('where is ', 1)[1]
        current_loc, target_loc, distance = obj.location(place)
        city = target_loc.get('city', '')
        state = target_loc.get('state', '')
        country = target_loc.get('country', '')
        time.sleep(1)
        try:

            if city:
                res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                print(res)
                speak(res)
            
            else:
                res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                print(res)
                speak(res)

        except:
            res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
            speak(res)