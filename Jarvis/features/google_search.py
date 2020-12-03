from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re, pyttsx3



def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 180)


def google_search(command):

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