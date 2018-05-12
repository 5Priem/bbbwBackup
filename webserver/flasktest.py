from flask import Flask
app = Flask(__name__)


counter=5

@app.route('/')
def hello_world():
	return str(counter)

if __name__ == '__main__':
	app.run(host='192.168.0.115')
