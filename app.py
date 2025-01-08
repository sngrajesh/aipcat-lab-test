import flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to CDAC!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)