DEBUG = False




try:
    from some.other.settings import * # All, Karl!
except ImportError:
    pass    # yeah, whatever.



import os

MY_TEMPLATES = os.path.join(os.path.dirname(__file__), 'templates')




import requests

globals().update(
    requests
        .get('http://example.com/settings.json')
        .json()
    )



# In your code

def get_template(name):
    dir = pathlib.Path(settings.MY_TEMPLATES)
    with (dir / name).open('rt') as f:
        return f.read()



def my_round(number):
    digits = getattr(settings, 'ROUND_DIGITS', 0)
    return round(number, digits)
