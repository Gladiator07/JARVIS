from Jarvis import JarvisAssistant
import json, re, random, pprint
obj = JarvisAssistant()

# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
"ok jarvis", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir", "your wish my command", "how can i help you sir?", "i am online and ready sir"]

NEWS = ["buzzing today", "top headlines", "news"]






# =======================================================================================================================================================
def speak(text):
    obj.tts(text)
while True:
    command = obj.mic_input()

    if re.search('date', command):
        date = obj.tell_me_date()
        print(date)
        speak(date)
    
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

    if re.search('weather|temperature', command):
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
            speak("Sorry sir. I couldn't load your query from my database. Please try again")

    if "buzzing today" in command or "news" in command:
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
