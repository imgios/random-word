import flask
from flask import request, jsonify
import random
import string

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def randomWord(word_length=8):
	"""Generate a random string of fixed lenght"""
	chars = string.ascii_letters + string.digits + string.punctuation
	return ''.join(random.choice(chars) for i in range(word_length))

@app.route('/', methods=['GET'])
def home():
	return "<h1>A basic API made in Python</h1><p>This website is a basic API prototype built with Python3 and Flask!</p>"
	
@app.route('/api/word', methods=['GET'])
def api_word():
	if 'length' in request.args:
		lenght = int(request.args['length'])
		res = jsonify({'status': 'OK', 'content': randomWord(lenght)})
		res.status_code = 200
		return res
	else:
		res = jsonify({'status': 'ERROR', 'content': 'No length field provided.'})
		res.status_code = 400
		return res

@app.errorhandler(404)
def not_found(error=None):
	res = jsonify({'status': 'ERROR', 'content': 'Not Found: ' + request.url})
	res.status_code = 404
	return res

app.run()
