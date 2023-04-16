from flask import Flask, render_template, render_template_string, request
from flask_socketio import SocketIO, emit
import flask

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

class run():
    socketio.run(app)