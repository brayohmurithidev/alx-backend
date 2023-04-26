#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel

'''
Basic Babel Setup
We instanciate babel object to our app.
Create config default locale to 'en' and timezone to 'UTC'
'''

app = Flask(__name__)
babel = Babel(app)


class Config:
    '''Config class'''
    LANGUAGES = ["en", "fr"]
    # Set the default locale to "en"
    BABEL_DEFAULT_LOCALE = 'en'
    # Set the default timezone to "UTC"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    '''Flask basic route'''
    return render_template("1-index.html")


if __name__ == "__main__":
    '''Run app'''
    app.run()
