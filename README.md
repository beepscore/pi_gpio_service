# Purpose
Make a simple Python flask web service to read and write Raspberry Pi GPIO.

# References

## Serving Raspberry Pi with Flask
http://mattrichardson.com/Raspberry-Pi-Flask/

## Raspberry Pi GPIO API
https://github.com/CorrosiveKid/raspberrypi-gpio-api

## Raspberry Pi Web Server using Flask to Control GPIOs
http://randomnerdtutorials.com/raspberry-pi-web-server-using-flask-to-control-gpios/

## Build a Python-powered web server with Flask
https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet

## basic_flask
https://github.com/beepscore/basic_flask
https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet


# Results

## RPi.gpio
miniconda didn't come with RPi.gpio.

ran

    conda install -c ericmjl ri.gpio

version 0.5.11 2016-12-01

Alternatively could use pypi package

    pip install into conda environmentbeepscore.

pypi version 0.5.7 date 2014

Package notes RPi.gpio library is not suitable for precise real time control. Linux may interrupt to garbage collect.
For timing critical applications use a microcontroller like Arduino.

