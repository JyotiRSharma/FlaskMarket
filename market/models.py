from market import db
from market import bcrypt

class User(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(length=30), nullable=False, unique=True)
	email_address = db.Column(db.String(length=50), nullable=False, unique=True)
	password_hash = db.Column(db.String(length=60), nullable=False)
	budget = db.Column(db.Integer(), nullable=False, default=1000)
	items = db.relationship('Item', backref='owned_user', lazy=True)  # back reference to the user from the Item table
	# lazy is used to grab all the items in one shot.

	@property
	def password(self):
		return self.password

	@password.setter
	def password(self, plain_text_password):  # **Over here - because we set a new password to new user
		self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

	def __repr__(self):
		return f'Item {self.name}'


class Item(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(length=30), nullable=False, unique=True)
	barcode = db.Column(db.String(length=12), nullable=False, unique=True)
	price = db.Column(db.Integer(), nullable=False)
	description = db.Column(db.String(length=1024), nullable=False, unique=True)
	owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

	def __repr__(self):
		return f'Item {self.name}'