# **FLASK QUICK START TEMPLATE**

### Requirements

Python 3.6+, pip, virtualenv

## Installation

First, clone this repository.

    $ git clone https://github.com/KarenNgala/flask-template
    $ cd flask-template

Create a virtualenv, and activate this: 

    $ virtualenv virtual 
    $ source virtual/bin/activate

Install pip into your virtual environment:

    $ curl https://bootstrap.pypa.io/get-pip.py | python

After, install all necessary requirements to run app:

    $ pip install -r requirements.txt

Then, run the application:

	$ python start.py server

To see your application, access this url in your browser: 

	http://localhost:5000

To run tests:

	$ python start.py test

All configurations are in: `config.py`