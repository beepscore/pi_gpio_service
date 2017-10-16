# Purpose
Make a simple Python flask web service to read and write Raspberry Pi GPIO.

# References

## Phoney
Phoney is an iOS application to experiment with testing phone calls.
https://github.com/beepscore/Phoney

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

## iPhone Headphone plug pinouts
http://www.friendmichael.com/Blog/iphone-headphone-plug-pinouts.html

##  iPad / iPhone / iPod Touch Microphone Adapter Wiring Diagram
http://www.blackcatsystems.com/ipad/iPad_iPhone_iPod_Touch_Microphone_Wiring.html

## How to Hack a Headphone Jack
http://www.circuitbasics.com/how-to-hack-a-headphone-jack/

# Results

## endpoints

### GET
e.g. use client browser or curl

    http://10.0.0.4:5000/api/v1/ping/
    http://10.0.0.4:5000/api/v1/gpio/status/
    
    read pin status
    http://10.0.0.4:5000/api/v1/gpio/<pin_number>/

### POST
e.g. use curl

    write a pin value
    http://10.0.0.4:5000/api/v1/gpio/<pin_number>/
    
    http://10.0.0.4:5000/api/v1/gpio/set-all-outputs-high/
    http://10.0.0.4:5000/api/v1/gpio/set-all-outputs-low/
    http://10.0.0.4:5000/api/v1/gpio/end-phone-call/

## Appendix install flask from anaconda/miniconda

Create anaconda environment

Activate anaconda environment

    source activate beepscore

Install flask

    conda install -n beepscore flask

## run on raspberry pi, view in macos browser
    python app.py

pi console shows Running on http://0.0.0.0:5000

### Fing
fing shows raspberry pi is on local network at 10.0.0.4  

    
## Appendix RPi.gpio
Package notes RPi.gpio library is not suitable for precise real time control.
Linux may interrupt to garbage collect.
For timing critical applications use a microcontroller like Arduino.

I think Raspbian comes with RPi.gpio
But program didn't see it, maybe not visible within conda environment.
miniconda didn't come with RPi.gpio.

### install with pip
with conda environment beepscore activated ran

    pip install RPi.GPIO


### initially installed with conda, package was out of date
with conda environment beepscore activated ran

    conda install -c ericmjl ri.gpio

This installed an older version 0.5.11 2016-12-01

I tried running
    python ./pi_gpio_service/service.py

RuntimeError: No access to /dev/mem. Try running as root!

Current version 0.6.3 doesn't require root.
https://raspberrypi.stackexchange.com/questions/40105/access-gpio-pins-without-root-no-access-to-dev-mem-try-running-as-root#40106
https://pypi.python.org/pypi/RPi.GPIO

#### In conda environment beepscore uninstall version 0.5.11

    conda list
    conda remove rpi.gpio
    

## Appendix switched jack for iPhone

The iDevice needs to see a resistance in the neighborhood of 5k between the microphone conductor and ground.
That tells it that a microphone has been plugged in.
If it is a direct short, it thinks a headphone was plugged in.
Open circuit means nothing was plugged in.
http://www.blackcatsystems.com/ipad/iPad_iPhone_iPod_Touch_Microphone_Wiring.html

