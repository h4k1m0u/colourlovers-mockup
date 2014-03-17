import sys
import logging
from colourlovers_mockup import app

# redirect wsgi app logging to apache stderr (error_log)
logging.basicConfig(stream=sys.stderr)

# add app path to python's path
sys.path.insert(0, "/home/hakim/public_html/flaskColourlovers")

# initialize wsgi app object
application = app
