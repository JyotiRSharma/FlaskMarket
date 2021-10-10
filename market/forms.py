from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(name=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists, try again!')

    def validate_email_address(self, email_to_check):
        email = User.query.filter_by(email_address=email_to_check.data).first()
        if email:
            raise ValidationError('Email already exists, try again!')

    username = StringField(label='User Name ', validators=[Length(min = 2, max = 30), DataRequired()])  # username should be min 2 to max 30
    email_address = StringField(label='Email Id ', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password ', validators=[Length(min = 6), DataRequired()])  # install flask_bcrypt to encrypt your passwords
    password2 = PasswordField(label='Confirm Password ', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

