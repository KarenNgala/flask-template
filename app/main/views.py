from . import main
from flask import render_template
from ..requests import *

@main.route('/')
def homepage():
    return render_template("index.html")
