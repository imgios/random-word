import flask
from flask import request, jsonify, render_template
import random
import string

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def randomWord(word_length=8, word_mode='strong'):
	"""Generate a random string of fixed lenght"""
	chars = string.ascii_letters # ASCII letters (weak setting)
	if word_mode == 'medium':
		chars += string.digits # ASCII letters + digits (medium setting)
	elif word_mode == 'strong':
		chars += string.digits  + string.punctuation # ASCII letters + digits + punctuation (strong setting)
		
	return ''.join(random.choice(chars) for i in range(word_length))

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title='Random-word API')
	
@app.route('/api/word', methods=['GET'])
def api_word():
	if 'length' in request.args:
		lenght = int(request.args['length'])
	else:
		res = jsonify({'status': 'ERROR', 'content': 'No length field provided.'})
		res.status_code = 400
		return res
	
	if 'mode' in request.args:
		mode = request.args['mode']
		if (mode.lower() == 'weak' or mode.lower() == 'medium' or mode.lower() == 'strong'):
			res = jsonify({'status': 'OK', 'content': randomWord(lenght, mode.lower())})
			res.status_code = 200
			return res
	else:
		res = jsonify({'status': 'OK', 'content': randomWord(lenght)})
		res.status_code = 200
		return res

@app.errorhandler(404)
def not_found(error=None):
	res = jsonify({'status': 'ERROR', 'content': 'Not Found: ' + request.url})
	res.status_code = 404
	return res

app.run()
