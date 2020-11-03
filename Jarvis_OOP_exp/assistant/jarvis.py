import threading
import speech_recognition as sr
from utils.utils import Utils
from intents.greeting import Greeting


class Jarvis:
    def __init__(self, logger, config):
        self.logger = logger
        self.config = config
        self.speech = sr.Recognizer()

    def get_voice_input(self):
        command = ''
        
        try:
            with sr.Microphone() as source:

                print("Listening:")
                self.speech.energy_threshold = 3000
                self.speech.adjust_for_ambient_noise(source, duration=1)
                audio = self.speech.listen(source=source, timeout=5, phrase_time_limit=5)

            command = self.speech.recognize_google(audio)
            self.logger.info('You said : {}'.format(command))

        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print('Network error')
        except sr.WaitTimeoutError:
            pass
        except TimeoutError:
            pass

        return command.lower()

    def run(self):
        while True:
            command = self.get_voice_input()
            for key in self.config:
                utterances = Utils.match_pattern(command, self.config[key]['utterances'])
                if utterances:
                    intent = key
                    response = Utils.choose_random(self.config[key]['response'])
                    break

            if intent == 'intent_greeting':
                greeting = Greeting(self.logger, response)
                greeting.speak()
                break
            
            # else:
            #     Utils.speak('Intent not found')