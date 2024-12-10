from flask import Flask
# from kupiapi import scraper


app = Flask(__name__)
@app.route("/")

def hello():
    return "<p>Hello, World!</p>"