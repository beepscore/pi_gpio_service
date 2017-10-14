#!/usr/bin/env/python3

""" A simple Python flask web service to read and write Raspberry Pi GPIO.
"""

from flask import Flask, jsonify, request
import RPi.GPIO as GPIO

# app is a flask object
app = Flask(__name__)

# https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering#12967
GPIO.setmode(GPIO.BCM)


# use pins dictionary to keep info "dry"
pins = {
    '23': {'name': 'IN_23', 'pin_direction': 'input'},
    '24': {'name': 'OUT_24', 'pin_direction': 'output'},
    '25': {'name': 'OUT_25', 'pin_direction': 'output'}
}


def input_pins(pins):
    """
    :param pins: dictionary of all pins, input and output
    :return: dictionary of pins configured as input
    """
    inputs = {}
    for key in pins.keys():
        if pins[key]['pin_direction'] == 'input':
            inputs[key] = pins[key]

    return inputs


def output_pins(pins):
    """
    :param pins: dictionary of all pins, input and output
    :return: dictionary of pins configured as output
    """
    outputs = {}
    for key in pins.keys():
        if pins[key]['pin_direction'] == 'output':
            outputs[key] = pins[key]

    return outputs


VALID_HIGH_VALUES = [1, '1', 'HIGH']
VALID_LOW_VALUES = [0, '0', 'LOW']


def configure_pin_as_input(pin_number):
    """
    :param pin_number: an integer
    """
    GPIO.setup(pin_number, GPIO.IN)


def configure_pin_as_output(pin_number):
    """
    :param pin_number: an integer
    """
    GPIO.setup(pin_number, GPIO.OUT)
    GPIO.output(pin_number, GPIO.LOW)


def configure_pins(pins):
    for pin_number_string in input_pins(pins).keys():
        configure_pin_as_input(int(pin_number_string))

    for pin_number_string in output_pins(pins).keys():
        configure_pin_as_output(int(pin_number_string))


def pin_status(pin_number_string):
    """
    :param pin_number_string: a string e.g. '24'
    :return:  python dictionary, can be jsonified
    """
    if pin_number_string in pins.keys():
        pin_number = int(pin_number_string)

        value = GPIO.input(pin_number)

        pin = pins[pin_number_string]
        data = {'pin_number': pin_number_string,
                'pin_name': pin['name'],
                'pin_direction': pin['pin_direction'],
                'value': value,
                'status': 'SUCCESS',
                'error': None}
    else:
        data = {'status': 'ERROR',
                'error': 'Invalid pin number.'}

    return data


def pin_update(pin_number_string, value):
    if pin_number_string in pins.keys():
        pin_number = int(pin_number_string)

        GPIO.output(pin_number, value)
        new_value = GPIO.input(pin_number)

        pin = pins[pin_number_string]
        data = {'pin_number': pin_number_string,
                'pin_name': pin['name'],
                'pin_direction': pin['pin_direction'],
                'new_value': new_value,
                'status': 'SUCCESS',
                'error': None}
    else:
        data = {'status': 'ERROR',
                'error': 'Invalid pin number or value.'}

    return data


configure_pins(pins)


# / is the website root, the entry point
# http://127.0.0.1:5000
# home http://127.0.0.1
# port :5000
@app.route('/')
@app.route("/api/v1/ping/", methods=['GET'])
def api_status():
    if request.method == 'GET':
        data = {'api_name': 'pi_gpio',
                'version': '1.0',
                'status': 'SUCCESS',
                'response': 'pong'}
        return jsonify(data)


@app.route("/api/v1/gpio/<pin_number_string>/", methods=['POST', 'GET'])
def gpio_pin(pin_number_string):
    if request.method == 'GET':
        data = pin_status(pin_number_string)

    elif request.method == 'POST':
        value = request.values['value']
        if value in VALID_HIGH_VALUES:
            data = pin_update(pin_number_string, 1)
        elif value in VALID_LOW_VALUES:
            data = pin_update(pin_number_string, 0)
        else:
            data = {'status': 'ERROR',
                    'error': 'Invalid value.'}
    return jsonify(data)


if __name__ == '__main__':
    try:
        # '0.0.0.0' accessible to any device on the network
        app.run(host='0.0.0.0', debug=True)
    except RuntimeError:
        pass
    finally:
        # fix RunTimeWarning This channel is already in use
        # may need to put in a try:catch:finally finally section to handle exceptions
        GPIO.cleanup()

