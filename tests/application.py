from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event
from hc_sr04 import HC_SR04
from servo import Servo

app = Flask(__name__)

#turn the flask app into a socketio app
socketio = SocketIO(app)

thread = Thread()
thread_stop_event = Event()

sensor = HC_SR04()
servo = Servo()

class Sonar(Thread):
    def __init__(self):
        self.delay = 0.5
        super(Sonar, self).__init__()

    def measure(self):
        while not thread_stop_event.isSet():
            ang = servo.move()
            dst = sensor.get_distance()
            socketio.emit('newdata', {'distance': dst, 'angle': ang}, namespace='/test')
            sleep(self.delay)

    def run(self):
        self.measure()

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the Sonar thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = Sonar()
        thread.start()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app.run(host='0.0.0.0',debug=True,port=8080))