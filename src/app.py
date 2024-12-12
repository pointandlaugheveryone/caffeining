from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from models import Base
import route
from flask import Flask, render_template, request, redirect, url_for, session
from models import Drink   
# from kupi import fetch_drinks


engine = create_engine(DATABASE_URI)        # init db connection
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)
@app.route('/')
def get_drinks():
    drinks = Drink.query.filter_by(discount=True).all()
    return render_template('home.html, drinks=drinks')

@app.route('/zero')
def get_zero_drinks():
    zero_drinks = Drink.query.filter_by(is_zero=True, discount=True).all()
    return render_template('zero.html', drinks=zero_drinks)

@app.route('/about')
def about_page():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
