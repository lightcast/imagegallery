#!flask/bin/python
import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads')
def uploads():
    return render_template('uploads.html')


if __name__ == '__main__':
    app.run(
        debug=True
    )
