import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
	return "<h1>A basic API made in Python</h1><p>This website a basic API prototype build with Python3 and Flask!</p>"
	
app.run()
