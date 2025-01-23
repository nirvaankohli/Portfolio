from flask import Flask, render_template, request, redirect, url_for, jsonify
from dotenv import load_dotenv
import json
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
