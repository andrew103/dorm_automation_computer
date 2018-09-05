from flask import Flask, jsonify, request, g, make_response
from flask import url_for, redirect, flash

app = Flask(__name__)

if __name__ == "__main__":
    app.secret_key = "dorm_comp_password"
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
