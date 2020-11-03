import threading
import speech_recognition as sr
from utils.utils import Utils

class Jarvis:
    def __init__(self, logger, config):
        self.logger = logger
        self.config = config
        self.speech = sr.Recognizer()

    def get_voice_input(self):
        command = ''
        r = self.sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening:")
                
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
                    response = Utils.choose_random(self.config[key]['response'])
                    break

            if key == 'intent_greeting':