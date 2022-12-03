from flask import Blueprint, request, session, redirect
from flask_backend.models.user import User
from flask_backend.services.utils import is_valid, getImage, valid_request

register_user = Blueprint('register_user', __name__)
@register_user.route('/register_user', methods = ['GET', 'POST'])


def show_register_user():
    if valid_request(request):
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        if is_valid(email, password):
            return 'Email already in use'

        User(username, email, password, getImage()).register_user()
        return redirect('http://localhost:3000/signin')



