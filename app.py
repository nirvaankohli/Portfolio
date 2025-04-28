from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/works')
def works():
    return render_template("works - home.html")

@app.route('/about')
def works():
    return render_template("about - home.html")
# Run the app
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
