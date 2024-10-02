from flask import Blueprint

core = Blueprint('core', __name__, template_folder='templates/core')

from blueprintapp.core import routes
