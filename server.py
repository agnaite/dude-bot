# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request
from flask_assets import Environment
from moody import chatbot
import os


app = Flask(__name__)
assets = Environment(app)


@app.route("/")
def home():

    question = request.args.get('question')

    if question:
        response = chatbot.get_response(question)

        return jsonify(response.text)
    else:
        return render_template('base.html')


if __name__ == "__main__":

    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = os.environ.get("DEBUG", True)

    extra_files = ['./templates/base.html', './static/css/styles.css']

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG, extra_files=extra_files)
