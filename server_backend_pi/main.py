from flask import Flask, jsonify, request, g, make_response
from flask import url_for, redirect, flash

app = Flask(__name__)

@app.route('/')
def index():
    return "Index page"

@app.route('/lights')
def lights():
    return "Lights"

@app.route('/lights_off')
def lights_off():
    return "Lights off"

@app.route('/fade_lights')
def fade_lights():
    return "Fade lights"

@app.route('/cancel')
def cancel():
    return "Cancel command"
