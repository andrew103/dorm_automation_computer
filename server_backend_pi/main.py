from flask import Flask, jsonify, request, g, make_response
from flask import url_for, redirect, flash
from _thread import start_new_thread
import pigpio
import time

RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24

app = Flask(__name__)
pi = pigpio.pi()

# Global variables for LED light control
bright = 255
abort = False
r = 255.0
g = 0.0
b = 0.0

def fadeLights():
    global r
    global g
    global b
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

@app.route('/')
def index():
    return "Index page"

@app.route('/lights')
@app.route('/lights_on')
def lights():
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
    abort = False
    start_new_thread(fadeLights, ())
    return "Fade lights"

@app.route('/cancel')
def cancel():
    return "Cancel command"
