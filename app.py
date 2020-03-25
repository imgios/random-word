import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
	return "<h1>A basic API made in Python</h1><p>This website a basic API prototype build with Python3 and Flask!</p>"

@app.route('/random', methods=['GET'])
def api_random():
	return "1SH0ULDBER4ND0M"
	
@app.route('/word', methods=['GET'])
def api_word():
	if 'lenght' in request.args:
		lenght = int(request.args['lenght'])
		return "Lenght field retrieved."
	else:
		return "ERROR: No 'lenght' field provided. Please, specify a lenght between 8 and 128."
	
app.run()
