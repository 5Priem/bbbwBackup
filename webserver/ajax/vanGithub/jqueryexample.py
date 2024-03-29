# -*- coding: utf-8 -*-
# https://github.com/pallets/flask/tree/0.12.4/examples/jqueryexample
from flask import Flask, jsonify, render_template, request
import mpu9250
app = Flask(__name__)

a = 4
try:
        mp1 = mpu9250.SL_MPU9250(0x68,2)
except:
        print("IMU's : Failed to import or execute mpu9250 library, IMU is probably not connected rightly")


@app.route('/_add_numbers')
def add_numbers():
    global a
    ax1, ay1, az1 = mp1.getAccel()
    ax1 = str(ax1)
    a = a+1#x#request.args.get('a', 0, type=int)
    b = 6#request.args.get('b', 0, type=int)
    return jsonify(result=ax1) #+ b)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='192.168.0.115')
