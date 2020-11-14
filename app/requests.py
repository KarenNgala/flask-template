from .models import *
import json, requests


key = None
url = None

def configure_request(app):
    global key, url
    key = app.config['API_KEY']
    # url = ...


# Add request functions here