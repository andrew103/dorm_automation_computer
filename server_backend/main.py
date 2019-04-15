from flask import Flask, jsonify, request, g, make_response
from flask import url_for, redirect, flash
from _thread import start_new_thread
import time
import yaml

app = Flask(__name__)
config = yaml.load(open('config.yaml'), Loader=yaml.Loader)

def updateConfig():
    global config
    config = yaml.load(open('config.yaml'), Loader=yaml.Loader)

@app.route('/')
def index():
    updateConfig()
    return "Index page"

@app.route('/lights')
def lights():
    updateConfig()
    return "Lights"

@app.route('/lights_off')
def lights_off():
    updateConfig()
    return "Lights off"

@app.route('/fade_lights')
def fade_lights():
    updateConfig()
    return "Fade lights"

@app.route('/cancel')
def cancel():
    updateConfig()
    return "Cancel command"
