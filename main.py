from Jarvis import JarvisAssistant
import json, re, random, pprint, webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request #used to make requests
import urllib.parse #used to parse values into the url



obj = JarvisAssistant()

# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
"ok jarvis", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir", "your wish my command", "how can i help you sir?", "i am online and ready sir"]







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

    
    # if re.search('open', command):
    #     domain = command.split(' ')[-1]
    #     open_result = obj.website_opener(domain)
    #     speak(f'Alright sir !! Opening {domain}')
    #     print(open_result)

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

    if 'search google for' in command:
            reg_ex = re.search('search google for (.*)', command)
            search_for = command.split("for", 1)[1]
            url = 'https://www.google.com/'
            if reg_ex:
                subgoogle = reg_ex.group(1)
                url = url + 'r/' + subgoogle
            speak("Okay sir!")
            speak(f"Searching for {subgoogle}")
            driver = webdriver.Chrome(
                executable_path='driver/chromedriver.exe')
            driver.get('https://www.google.com')
            search = driver.find_element_by_name('q')
            search.send_keys(str(search_for))
            search.send_keys(Keys.RETURN)

    
    # elif 'youtube' in command:
    #     speak('Ok!')
    #     reg_ex = re.search('youtube (.+)', command)
    #     if reg_ex:
    #         domain = command.split("youtube",1)[1] 
    #         query_string = urllib.parse.urlencode({"search_query" : domain})
    #         html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string) 
    #         search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode()) # finds all links in search result
    #         webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))
    #         pass

