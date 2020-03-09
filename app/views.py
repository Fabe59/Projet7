from flask import Flask, render_template, jsonify, request

from app.services import Services

from . import app


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["userText"]

    services = Services()
    response = services.services(user_text)

    return jsonify(response)