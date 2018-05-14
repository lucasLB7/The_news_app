from flask_bootstrap import Bootstrap
from flask import Blueprint


main = Blueprint('main', __name__)

from . import views, error

