from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from models import Base
# from kupiapi import scraper


app = Flask(__name__)
@app.route("/")

def hello():
    return "<p>Hello, World!</p>"
