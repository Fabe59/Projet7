from flask import render_template, request, escape

from app.services import Services
from settings.config import key_google_map_api

from . import app


@app.route("/")
def home():
    return render_template("index.html", api_key=key_google_map_api)


@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["userText"]
    services = Services()
    response = services.services("%s" % escape(user_text))
    return response
