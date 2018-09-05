from flask import Flask, jsonify, request, g, make_response
from flask import url_for, redirect, flash

app = Flask(__name__)

@app.route('/')
def index():
    return "Index page"
