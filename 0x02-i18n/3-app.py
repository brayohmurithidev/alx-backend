#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

'''
Parametrize templates
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


@babel.localeselector
def get_locale():
    '''get Locale function'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def basic_flask():
    '''Flask basic route'''
    title = _("Welcome to Holberton")
    header = _("Hello world")
    return render_template("3-index.html", title=title, header=header)


if __name__ == "__main__":
    app.run(debug=True)
