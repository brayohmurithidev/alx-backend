#!/usr/bin/env python3

'''
Basic flask
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def basic_flask():
    '''Flask basic route'''
    title = "Welcome to Holberton"
    header = "Hello world"
    return render_template("0-index.html", title=title, header=header)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
