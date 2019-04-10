from flask import Flask, jsonify, request, g, make_response
from flask import url_for, redirect, flash
import pigpio
import time

RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24

app = Flask(__name__)
pi = pigpio.pi()

# Global variables for LED light control
bright = 255
r = 0
g = 0
b = 0

def setLights(pin, brightness):
    realBrightness = int(int(brightness) * (float(bright) / 255.0))
    pi.set_PWM_dutycycle(pin, realBrightness)

@app.route('/')
def index():
    return "Index page"

@app.route('/lights')
def lights():
    for i in range(256):
        global bright
        bright = i
        setLights(RED_PIN, 255)
        setLights(GREEN_PIN, 147)
        setLights(BLUE_PIN, 41)
        time.sleep(0.005)

    return "Lights"

@app.route('/lights_off')
def lights_off():
    global bright
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
    return "Fade lights"

@app.route('/cancel')
def cancel():
    return "Cancel command"
