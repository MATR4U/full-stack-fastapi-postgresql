
from flask import Blueprint
from utils import generate_numbers, render_table

main = Blueprint('main', __name__)

@main.route('/')
def index():
    numbers = generate_numbers()
    return render_table(numbers)
