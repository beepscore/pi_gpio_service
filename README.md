# Purpose
Make a simple Python flask web service to read and write Raspberry Pi GPIO.

# Results

## service_piface.py
Uses PiFace.
must run as sudo, else library not found?

    sudo python3 ./pi_gpio_service/service_piface.py

### endpoints

#### GET
e.g. use client browser or curl

    http://10.0.0.4:5000/api/v1/ping/

#### POST
e.g. use curl

    http://10.0.0.4:5000/api/v1/gpio/end-phone-call/


## service.py
Uses gpio pins, not PiFace

    python3 ./pi_gpio_service/service.py

### endpoints

#### GET
e.g. use client browser or curl

    http://10.0.0.4:5000/api/v1/ping/
    http://10.0.0.4:5000/api/v1/gpio/status/
    
    read pin status
    http://10.0.0.4:5000/api/v1/gpio/<pin_number>/

#### POST
e.g. use curl

    write a pin value
    http://10.0.0.4:5000/api/v1/gpio/<pin_number>/
    
    http://10.0.0.4:5000/api/v1/gpio/set-all-outputs-high/
    http://10.0.0.4:5000/api/v1/gpio/set-all-outputs-low/
    http://10.0.0.4:5000/api/v1/gpio/end-phone-call/

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

## Appendix PiFace

### Hardware

#### Distributors

##### PiFace Digital 2 (Relay and Interface HAT Pi Face)
SKU: VET-PIFC2
https://vetco.net/products/piface-digital-2-relay-and-interface-hat-pi-face

##### Element 14
https://www.element14.com/community/docs/DOC-69001/l/piface-digital-2-for-raspberry-pi

#### Manufacturer
http://www.piface.org.uk/products/piface_digital/
http://www.piface.org.uk/assets/docs/PiFace-Digital2_getting-started.pdf
http://www.piface.org.uk/guides/
http://www.piface.org.uk/guides/simple_web_control_with_piface_digital/getting_started_simple_web_control_piface_digital/

### Setup

## Warnings
Ensure that no power is supplied to Raspberry Pi or PiFace Digital 2 boards when plugging or unplugging.

## jumpers
### function
1 sets board address bit 0
2 sets board address bit 1
3 Connects PiFace digital 5v to raspberry pi 5v. SEE WARNING
4 Connects snubber diodes to 5v
5 Connects relay 0
6 Connects relay 1
7 connects 5v power to LEDs and relay coils

### jumper factory settings
1 connects 1-2 (0)
2 connects 1-2 (0)
3 connected SEE WARNING
4 Connects snubber diodes to 5v
5 connected
6 connected
7 connected

### jumper my settings
1 connects 1-2 (0)
2 connects 1-2 (0)
3 connected SEE WARNING
4 Connects snubber diodes to 5v
5 connected
6 connected
7 connected

## JP3
Power share jumper
JP3 selects whether the PiFace™ Digital 2 shares the same power source as the
Raspberry Pi®. This supply can be either provided through the Raspberry Pi®’s MicroUSB
connector, or from an external supply provided through PiFace™ Digital 2’s 5V and GND
power screw terminals. With the jumper connected, the Raspberry Pi® and  PiFace™
Digital 2 will share a single power supply. Disconnected, they will each need to be powered
separately.

### WARNING:
never use separate power supplies for both the raspberry pi® and piface™ digital 2,
when this jumper is connected.

// TODO: disconnect to maximize isolation between pi and controlled device
*After* disconnecting, connect separate 5v supply

## JP4
Snubber diodes jumper
JP4 connects the snubber diodes from the ULN2803A to 5V (snubber diodes protect the
driving transistors from the high voltages that occur when a coil, e.g. a relay, turns off).

### HOWEVER
if the open-collectors are connected to a supply greater than 5v, these diodes
must be disconnected by removing jp4 (else the diodes will conduct between the outputs and 5v).

ULN2803A darlington transistors eight npn array
==> use supply <= 5v, leave JP4 connected.

## SPI
The SPI interface driver must be enabled using raspi-config.

    sudo raspi-config

Board documentation says look in "Advanced". I think this is out of date.
I found it under "Interfacing options".

### board emulator (not necessary)

    pifacedigital-emulator

requires running X window

## python3

### python library

    sudo apt-get install python3-pifacedigitalio

Apparently it was already installed. "python3-pifacedigitalio is already the newest version."

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

#### iPhone Headphone plug pinouts
http://www.friendmichael.com/Blog/iphone-headphone-plug-pinouts.html

#### iPad / iPhone / iPod Touch Microphone Adapter Wiring Diagram
http://www.blackcatsystems.com/ipad/iPad_iPhone_iPod_Touch_Microphone_Wiring.html  

The iDevice needs to see a resistance in the neighborhood of 5k between the microphone conductor and ground.
That tells it that a microphone has been plugged in.
If it is a direct short, it thinks a headphone was plugged in.
Open circuit means nothing was plugged in.

#### How to Hack a Headphone Jack
http://www.circuitbasics.com/how-to-hack-a-headphone-jack/

