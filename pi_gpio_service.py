#!/usr/bin/python3

""" A simple Python flask web service to read and write Raspberry Pi GPIO.
"""

from flask import Flask, jsonify, request
# import RPi.GPIO as GPIO

# app is a flask object
app = Flask(__name__)

# https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering#12967
# GPIO.setmode(GPIO.BCM)


# use pins dictionary to keep info "dry"
pins = {'23': {'name': 'IN_23', 'pin_direction': 'input'},
        '24': {'name': 'OUT_24', 'pin_direction': 'output'},
        '25': {'name': 'OUT_25', 'pin_direction': 'output'}
       }


def input_pins():
    return [pin for pin in pins if pin['pin_direction'] == 'input']


def output_pins():
    return [pin for pin in pins if pin['pin_direction'] == 'output']


VALID_HIGH_VALUES = [1, '1', 'HIGH']
VALID_LOW_VALUES = [0, '0', 'LOW']


# def configure_pin_as_input(pin_number):
#     GPIO.setup(pin_number, GPIO.IN)


# def configure_pin_as_output(pin_number):
#     GPIO.setup(pin_number, GPIO.OUT)
#     GPIO.output(pin_number, GPIO.LOW)


# def configure_pins():
#     for pin in input_pins():
#         configure_pin_as_input(pin)
# 
#     for pin in output_pins():
#         configure_pin_as_output(pin)


# def pin_status(pin_number_string):
#     if pin_number in pins:
#         value = GPIO.input(pin_number)
#         data = {'pin_number': pin_number,
#                 'pin_name': pins[pin_number],
#                 'value': value,
#                 'status': 'SUCCESS',
#                 'error': None}
#     else:
#         data = {'status': 'ERROR',
#                 'error': 'Invalid pin number.'}
# 
#     return data


# def pin_update(pin_number, value):
#     if pin_number in pins.keys:
#         GPIO.output(pin_number, value)
#         new_value = GPIO.input(pin_number)
#         data = {'status': 'SUCCESS',
#                 'error': None,
#                 'pin_number': pin_number,
#                 'pin_name': pins[pin_number],
#                 'new_value': new_value}
#     else:
#         data = {'status': 'ERROR',
#                 'error': 'Invalid pin number or value.'}
# 
#     return data


# configure_pins()

# / is the website root, the entry point
# http://127.0.0.1:5000
# home http://127.0.0.1
# port :5000
@app.route('/')
@app.route("/api/v1/ping/", methods=['GET'])
def api_status():
    if request.method == 'GET':
        data = {'api_name': 'pi_gpio_service',
                'version': '1.0',
                'status': 'SUCCESS',
                'response': 'pong'}
        return jsonify(data)


# @app.route("/api/v1/gpio/<pin_number_string>/", methods=['POST', 'GET'])
# def gpio_pin(pin_number_string):
#     pin_number = int(pin_number_string)
#     if request.method == 'GET':
#         data = pin_status(pin_number)
# 
#     elif request.method == 'POST':
#         value = request.values['value']
#         if value in VALID_HIGH_VALUES:
#             data = pin_update(pin_number, 1)
#         elif value in VALID_LOW_VALUES:
#             data = pin_update(pin_number, 0)
#         else:
#             data = {'status': 'ERROR',
#                     'error': 'Invalid value.'}
#     return jsonify(data)

if __name__ == '__main__':
    # '0.0.0.0' accessible to any device on the network
    app.run(host='0.0.0.0', debug=True)
