from flask import Blueprint

people = Blueprint('people', __name__, template_folder='templates/people')

from blueprintapp.people import routes
