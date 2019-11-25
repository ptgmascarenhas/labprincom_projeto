from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route("/")
def main():
	return "Vá para /mapa"

@app.route("/mapa")
def mapear():	
	return render_template("index_image.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True,port=8080)
