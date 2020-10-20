import time

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():

    now = time.localtime()

    return f"""
<h1> Welcome! </h1>

It is {now.tm_hour}:{now.tm_min:02} on {now.tm_mday}/{now.tm_mon}/{now.tm_year}.
"""

@app.route('/secret') #if they type the url/secret, they get a special response 'you found me'
def secret():
    return 'You found me!'

