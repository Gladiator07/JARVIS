import threading
import speech_recognition as sr
from utils.utils import Utils
from intents.greeting import Greeting


class Jarvis:
    def __init__(self, logger, config):
        self.logger = logger
        self.config = config
        self.speech = sr.Recognizer()
        threading.Thread(target=self.run().start())

    def read_voice(self):
        voice_input = ''
        try:
            with sr.Microphone() as source:
                audio = self.speech.listen(
                    source=source, timeout=5, phrase_time_limit=5)
            voice_input = self.speech.recognize_google(audio)
            self.logger.info(f'You said : {voice_input}')

        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print('Network Error')
        except sr.WaitTimeoutError:
            pass
        except TimeoutError:
            pass
        return voice_input.lower()

    def run(self):
        while True:
            voice_note = self.read_voice()
            for key in self.config:
                Utils.match_pattern(voice_note, self.config[key]['utterances'])
                if utterances:
                    response = Utils.choose_random(
                        self.config[key]['response'])
                    break
            if key == 'intent_greeting':
                Greeting(self.logger, response)
                break
            else:
                Utils.tts('Sorry sir I could not understand)
