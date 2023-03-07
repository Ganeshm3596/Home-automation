from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

lights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
appliances = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

GPIO.setup(lights, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(appliances, GPIO.OUT, initial=GPIO.LOW)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/light', methods=['POST'])
def light():
    light_num = request.form['light_num']
    status = request.form['status']
    if status == 'on':
        GPIO.output(lights[int(light_num) - 1], GPIO.HIGH)
    else:
        GPIO.output(lights[int(light_num) - 1], GPIO.LOW)
    return 'success'

@app.route('/appliance', methods=['POST'])
def appliance():
    appliance_num = request.form['appliance_num']
    status = request.form['status']
    if status == 'on':
        GPIO.output(appliances[int(appliance_num) - 1], GPIO.HIGH)
    else:
        GPIO.output(appliances[int(appliance_num) - 1], GPIO.LOW)
    return 'success'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
