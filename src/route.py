from flask import Flask, render_template, request, redirect, url_for, session
# from models import db, Drink   
# from api import fetch_drinks

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