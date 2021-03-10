# This is a sample Python script.

# This runs home.html


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Imports
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from flask import Flask, render_template, request

app = Flask(__name__)
bot = ChatBot("Pikachu")

trainer = ListTrainer(bot)

trainer.train(['What is your name?', 'My name is Pikachu'])
trainer.train(['How are you?', 'I am good'])
trainer.train(['Bye?', 'Bye, see you later'])

conversation = [
    "Hello",
    "Hello!!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer.train(conversation)

corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Test Chat Bot')
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
