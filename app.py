from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
import json
import os

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/works')
def works():
    return render_template("works - home.html")

@app.route('/about')
def about():
    return render_template("about - home.html")
# Run the app
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
