from flask import Flask, render_template, request
from hc_sr04 import HC_SR04
import time
import random
from time import sleep

mapa = []

app = Flask(__name__)

@app.route("/")
def main():
	return "Vá para /mapa"
    
@app.route("/mapa")
def mapear():
	for i in range(0, 180):
		dst = random.randint(0, 300)
		medida = {'angle': i, 'distance': dst}
		mapa.append(medida)
		
	return str(mapa)

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True,port=8080)
