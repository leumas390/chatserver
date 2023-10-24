from flask import Flask, render_template
from flask_socketio import SocketIO, send

#Flask-socketIO allow to work socket easily with Flask in the backend

app = Flask(__name__)
app.config['SECRET'] =  "secret!123"
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(message):
    print("Received message: " + message) #display the messsege sent by the user
    if message != "User Connected!": #message will display every time an user connects to the server
        send(message, broadcast=True)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host="localhost") #to connect multiple devices change "localhost" to private IP address