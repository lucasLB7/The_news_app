from flask_bootstrap import Bootstrap
from flask import Blueprint


main = Blueprint('login', __name__)

from . import views, error
