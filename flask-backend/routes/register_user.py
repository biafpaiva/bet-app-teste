from flask import Blueprint, request, session, redirect
from models.user import User
from services.utils import is_valid, getImage

register_user = Blueprint('register_user', __name__)
@register_user.route('/register_user', methods = ['GET', 'POST'])

def show_register_user():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        if is_valid(email, password):
            return 'Email already in use'
        else:
            User(username, email, password, getImage()).register_user()
            return redirect('http://localhost:3000/signin')