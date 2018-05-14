from flask import Flask, flash, redirect, render_template, request, session, abort
import mpu9250
import Adafruit_BBIO.GPIO as GPIO
import time
import os

app = Flask(__name__)


try:
	mp1 = mpu9250.SL_MPU9250(0x68,2)
except:
	print("IMU's : Failed to import or execute mpu9250 library, IMU is probably not connected rightly")

counter=5
vaaar = "bijour"

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/hello/<string:vaaar>/")
def varMeegeven(vaaar):
    return render_template('index.html', vaaar=vaaar)

@app.route('/test')
def test():
    try:
        ax1, ay1, az1 = mp1.getAccel()
        ax1 = str(ax1)
    except:
        ax1="mpu value not found"
    return render_template('index.html', ax1=ax1)


if __name__ == '__main__':
	app.run(host='192.168.0.115')
