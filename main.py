from Jarvis import JarvisAssistant
import json, re, random
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
    
    if re.search('launch', command):
        dict_app = {
            'chrome': 'C:\Program Files\Google\Chrome\Application\chrome'
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
        
# def speak(text):
#     obj.tts(text)
# memory = obj.read_json()
# # command = obj.mic_input()


# if re.search('date', command):
#     date = obj.tell_me_date()
#     print(date)
#     speak(date)
