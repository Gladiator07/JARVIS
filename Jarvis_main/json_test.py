import json

def read_config():
    with open('config.json') as file:
        data = json.load(file)
        for intent in data:
            print(intent)

read_config()