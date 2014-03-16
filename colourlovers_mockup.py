#!/usr/bin/python

from flask import Flask, render_template
from colourlovers import ColourLovers
import os

# create app
app = Flask(__name__)

# routes
@app.route('/')
def home():
    # get a random palette
    cl = ColourLovers()
    palette = cl.palettes('random').pop()
    palette_id, palette_title, colours = palette.id, palette.title, palette.colours

    return render_template('mockup.html', **{
        'colour1': colours[0],
        'colour2': colours[1],
        'colour3': colours[2],
        'colour4': colours[3],
        'colour5': colours[4],
        'palette_id': palette_id,
        'palette_title': palette_title,
        'getmtime': os.path.getmtime
    })

# run app
if __name__ == '__main__':
    app.run(debug=True)    
