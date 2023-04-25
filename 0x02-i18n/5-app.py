from flask import Flask, g, render_template, request

app = Flask(__name__)

# Define user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Define get_user function
def get_user():
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    else:
        return None

# Define before_request function to set up g.user
@app.before_request
def before_request():
    g.user = get_user()

# Define home route
@app.route('/')
def home():
    if g.user:
        message = {'en': f"You are logged in as {g.user['name']}.",
                   'fr': f"Vous êtes connecté en tant que {g.user['name']}."}
    else:
        message = {'en': "You are not logged in.",
                   'fr': "Vous n'êtes pas connecté."}
    return render_template('5-index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
