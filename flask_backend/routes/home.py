from flask import Blueprint
from flask_backend.services.utils import getLoginDetails

home = Blueprint('home', __name__)
@home.route("/")

def show_home():
    loggedIn, username = getLoginDetails()
    data = str(username)
    return data if loggedIn else 'user not found'