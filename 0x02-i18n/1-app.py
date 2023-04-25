#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel

'''
Basic Babel Setup
'''


class Config:
    '''Config class'''
    LANGUAGES = ["en", "fr"]
    # Set the default locale to "en"
    BABEL_DEFAULT_LOCALE = 'en'
    # Set the default timezone to "UTC"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def basic_flask():
    '''Flask basic route'''
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
