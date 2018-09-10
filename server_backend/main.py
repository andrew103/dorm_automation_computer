from flask import Flask, jsonify, request, g, make_response
from flask import url_for, redirect, flash

app = Flask(__name__)

@app.route('/')
def index():
    return "Index page"

@app.route('/lights')
def lights():
    pass

@app.route('/lights_off')
def lights_off():
    pass

@app.route('/fade_lights')
def fade_lights():
    pass
