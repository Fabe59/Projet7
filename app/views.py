from flask import Flask, render_template, jsonify, request
from parser import Parser
from googlemaps import GoogleMaps

from . import app


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["userText"]

    test_parser = Parser(user_text)
    response = test_parser.parsing_lowercase()
    response = test_parser.parsing_ponctuation()
    response = test_parser.split_sentence()
    response = test_parser.parsing_stopwords()

    #test_google = GoogleMaps()
    #google_response = test_google.get_coordinates(response)

    return jsonify(response)