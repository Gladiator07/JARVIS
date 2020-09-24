import requests

sender = input("What is your name?\n")
bot_message = ""

while bot_message != "Bye":
    message = input("What's your message?\n")

    print("Sending message now....")


    r = requests.post('http://localhost:5002/webhooks/rest/webhook',
    json = {"sender": sender, "message": message})

    print("Bot says, ", end=' ')

    for i in r.json():
        bot_message = i["text"]
        print(f"{i['text']}")