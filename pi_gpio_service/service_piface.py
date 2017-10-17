#!/usr/bin/env/python3

""" A simple Python flask web service to read and write Raspberry Pi PiFace digital 2 board.
"""

from flask import Flask, jsonify, request

# must run as sudo, else not found?
import pifacedigitalio

from time import sleep

# app is a flask object
app = Flask(__name__)

# must initialize PiFace board before use
pifacedigitalio.init()

pfd = pifacedigitalio.PiFaceDigital()


def end_phone_call():
    """
    simulate manually clicking headphone switch to end a phone call
    :return: result of last pin_update
    """

    relay0 = pfd.output_pins[0]
    relay1 = pfd.output_pins[1]

    # turn relay0 on
    relay0.value = 1

    delay_seconds = 0.2
    sleep(delay_seconds)

    # turn relay0 off
    relay0.value = 0

    data = {'api_name': 'pi_gpio',
            'version': '1.0',
            'status': 'SUCCESS',
            'response': 'end_call_response'}

    return jsonify(data)


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


# POST but not GET because GET should not change any state on the server
@app.route("/api/v1/gpio/end-phone-call/", methods=['POST'])
def gpio_end_phone_call():
    return end_phone_call()


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

