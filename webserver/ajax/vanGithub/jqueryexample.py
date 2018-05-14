# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

a = 4

@app.route('/_add_numbers')
def add_numbers():
    global a
    a = a + 1#request.args.get('a', 0, type=int)
    b = 6#request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='192.168.0.115')
