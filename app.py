from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.chinese")

import process_model as pm
def response_text(text):
    processed_text = pm.response(text)
    return processed_text


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    processed_text = response_text(userText)
    return (str(english_bot.get_response(userText)) + '(' + processed_text + ')')


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8888)
