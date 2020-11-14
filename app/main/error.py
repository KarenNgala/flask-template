from flask import render_template
from . import main

@main.app_errorhandler(404)
def not_found(error):
    ''' function to display error page '''
    return render_template('error.html'), 404