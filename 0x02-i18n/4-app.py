#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

'''
 Force locale with URL parameter
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
    # Check if the locale parameter is present in the request
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def basic_flask():
    '''Flask basic route'''
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
