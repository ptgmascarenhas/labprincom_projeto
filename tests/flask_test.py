from flask import Flask, render_template, request
from hc_sr04 import HC_SR04
import time

sensor = HC_SR04()

app = Flask(__name__)

@app.route("/")
def main():
    dst = sensor.get_distance()
    return str(dst)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=8080)
