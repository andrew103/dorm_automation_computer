from flask import Flask, jsonify, request, g, make_response
from flask import url_for, redirect, flash
from _thread import start_new_thread
import pigpio
import time
import yaml

app = Flask(__name__)
pi = pigpio.pi()
config = yaml.load(open('config.yaml'), Loader=yaml.Loader)

# Global variables for LED light control
RED_PIN = config['data']['constants']['RED_PIN']
GREEN_PIN = config['data']['constants']['GREEN_PIN']
BLUE_PIN = config['data']['constants']['BLUE_PIN']

bright = 255
abort = False
r = 255.0
g = 0.0
b = 0.0

def fadeLights(r, g, b):
#    global r
#    global g
#    global b
    while not abort:
        if r == 255 and b == 0 and g < 255:
            g += 1
            if g > 255:
                g = 255
            setLights(GREEN_PIN, g)
        elif g == 255 and b == 0 and r > 0:
            r -= 1
            if r < 0:
                r = 0
            setLights(RED_PIN, r)
        elif r == 0 and g == 255 and b < 255:
            b += 1
            if b > 255:
                b = 255
            setLights(BLUE_PIN, b)
        elif r == 0 and b == 255 and g > 0:
            g -= 1
            if g < 0:
                g = 0
            setLights(GREEN_PIN, g)
        elif g == 0 and b == 255 and r < 255:
            r += 1
            if r > 255:
                r = 255
            setLights(RED_PIN, r)
        elif r == 255 and g == 0 and b > 0:
            b -= 1
            if b < 0:
                b = 0
            setLights(BLUE_PIN, b)

        time.sleep(0.002)

def setLights(pin, brightness):
    realBrightness = int(int(brightness) * (float(bright) / 255.0))
    pi.set_PWM_dutycycle(pin, realBrightness)

def updateConfig():
    global config
    config = yaml.load(open('config.yaml'), Loader=yaml.Loader)

@app.route('/')
def index():
    updateConfig()
    return "Command does not exist"

@app.route('/lights')
@app.route('/lights_on')
def lights():
    updateConfig()
    global bright
    global abort
    abort = True
    for i in range(256):
        bright = i
        setLights(RED_PIN, 255)
        setLights(GREEN_PIN, 147)
        setLights(BLUE_PIN, 41)
        time.sleep(0.005)

    return "Lights"

@app.route('/lights_off')
def lights_off():
    updateConfig()
    global bright
    global abort
    abort = True
    for i in reversed(range(256)):
        bright = i
        setLights(RED_PIN, 255)
        setLights(GREEN_PIN, 147)
        setLights(BLUE_PIN, 41)
        time.sleep(0.005)

    bright = 255
    setLights(RED_PIN, 0)
    setLights(GREEN_PIN, 0)
    setLights(BLUE_PIN, 0)
    return "Lights off"

@app.route('/fade_lights')
def fade_lights():
    updateConfig()
    global r, g, b
    abort = False
    start_new_thread(fadeLights, (r, g, b))
    return "Fade lights"

@app.route('/cancel')
def cancel():
    updateConfig()
    return "Cancel command"
