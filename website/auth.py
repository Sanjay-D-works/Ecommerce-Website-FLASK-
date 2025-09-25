from flask import Blueprint, render_template
from .forms import LoginForm, SingUpForm

auth = Blueprint('auth', __name__)


@auth.route('/sign-up')
def sign_up():
    form = SingUpForm


    return render_template('signup.html', form=form)


@auth.route('/login')
def login():

    return 'This is the login page'

