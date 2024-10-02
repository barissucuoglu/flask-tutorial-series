from flask import Blueprint

todos = Blueprint('todos', __name__, template_folder='templates/todos')

from blueprintapp.todos import routes
