from flask import Flask, render_template, request, send_file
from hc_sr04 import HC_SR04
import time
import random
from time import sleep
from plot_graph import get_graph

app = Flask(__name__)

@app.route("/")
def main():
	return "Vá para /mapa"
    
@app.route("/mapa")
def mapear():
	get_graph()
	return render_template("index_image.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True,port=8080)
