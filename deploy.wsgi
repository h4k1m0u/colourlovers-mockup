#!/usr/bin/python

# add app path to python's path
import sys
sys.path.insert(0, "/home/hakim/public_html/flaskColourlovers")

# initialize wsgi app object
from colourlovers_mockup import app
application = app
