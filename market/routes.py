# import app
# from flask import render_template
# from models import Item

from market import app
from flask import render_template, redirect, url_for, flash
from market import forms
from market.models import Item, User
from market.forms import RegisterForm
from market import db


@app.route('/')
@app.route('/home')
def home_page():
	return render_template('home.html')


@app.route('/market')
def market_page():
	items = Item.query.all()
	return render_template('market.html', items=items)


@app.route('/users')
def show_users():
	# users = User.query.all()
	users = db.engine.execute('SELECT id, name, email_address, budget FROM user;')
	return render_template('users.html', items=users)


@app.route('/register', methods=['GET', 'POST'])
def register_form():
	form = RegisterForm()
	if form.validate_on_submit():
		user_to_create = User(
			name=form.username.data, 
			email_address=form.email_address.data, 
			password=form.password1.data)  # password is stored in a Hash algo sent to the models**
		db.session.add(user_to_create)
		db.session.commit()
		return redirect(url_for('market_page'))

	if form.errors !=  {}:  # if there are error in the form
		# print(form.errors)
		for key, err_msg in form.errors.items():
			flash(f"The error was with {key} as {err_msg}", category="danger")

	return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
	return render_template('login.html')

