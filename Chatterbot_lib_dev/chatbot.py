from chatterbot import ChatBot
from chatterbot.trainers import ChatterbotCorpusTrainer


# Create a chatbot

chatbot = ChatBot('jarvis')
trainer = ChatterbotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

while True:
    query = str(input(">>"))
    print(chatbot.get_response(query))
    if "exit" in query:
        break