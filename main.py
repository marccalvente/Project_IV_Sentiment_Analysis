from flask import Flask, request, jsonify
import random
import numpy as np
import markdown.extensions.fenced_code
import tools.sql_queries as esecuele
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


app = Flask(__name__)

# Render the markdwon
@app.route("/")
def readme ():
    readme_file = open("README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])

# GET ENDPOINTS: SQL 
# SQL get everything
@app.route("/sql/")
def sql ():
    return jsonify(esecuele.get_everything())

@app.route("/sql/name/<username>", )
def messages_from_user (username):
    return jsonify(esecuele.get_everything_from_user(username))


@app.route("/sql/date/<date>/", )
def messages_from_date (date):
    everything = esecuele.get_messages_from_date(date)
    return jsonify(everything)

@app.route("/sql/messages_score")
def messages_score ():
    return jsonify(esecuele.get_messages_score())


@app.route("/sql/emojis_score")
def emojis_score ():
    return jsonify(esecuele.get_emojis_score())


####### POST
@app.route("/insertrow", methods=["POST"])
def try_post ():
    # Decoding params
    my_params = request.args
    id = my_params.name
    date = my_params["date"]
    username = my_params["username"]
    message = my_params["message"]
    emojis = my_params["emojis"]
    message_translated = my_params["message_translated"]
    message_score = my_params["message_score"]
    emojis_score = my_params["emojis_score"]


    esecuele.insert_one_row(id,date, username, message, emojis, message_translated, message_score, emojis_score)
    return f"Query succesfully inserted"


if __name__ == "__main__":
    app.run(port=9000, debug=True)


