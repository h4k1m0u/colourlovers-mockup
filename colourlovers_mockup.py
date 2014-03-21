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
        'colour1': get_colour(colours, 0),
        'colour2': get_colour(colours, 1),
        'colour3': get_colour(colours, 2),
        'colour4': get_colour(colours, 3),
        'colour5': get_colour(colours, 4),
        'palette_id': palette_id,
        'palette_title': palette_title,
        'mtime': str(os.path.getmtime(app.root_path + '/static/style.css'))
    })

def get_colour(l, i):
    """ Returns colour of index 'i' from list 'l' if it exists, else return #00000
      Args:          
          l (list): list of colours
          i (int): index of the colour to get
      Returns:       
          colour (int): colour returned
    """
    try:
        colour = l[i]
    except IndexError:
        colour = '#000000'

    return colour

# run app
if __name__ == '__main__':
    app.run(debug=True)    
