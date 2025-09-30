from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, PasswordField, EmailField, BooleanField, SubmitField
from wtforms.validators import DataRequired, length, NumberRange


class SingUpForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), length(min=2)])
    password1 = PasswordField('Enter Your Password', validators=[DataRequired(), length(min=6)])
    password2 = PasswordField('confirm Your Password', validators=[DataRequired(), length(min=6)])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Enter your Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class PasswordChangeForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired(), length(min=6)])
    new_password = PasswordField('New Password', validators=[DataRequired(), length(min=6)])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), length(min=6)])
    change_passowrd = SubmitField('Change Password')
    