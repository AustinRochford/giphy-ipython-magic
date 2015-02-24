from IPython.display import Image

import requests

API_ENDPOINT = 'http://api.giphy.com/v1/gifs/random'
API_KEY = 'dc6zaTOxFJmzC'

def giphy(tag):
    params = {
        'api_key': API_KEY,
        'tag': tag
    }

    r = requests.get(API_ENDPOINT, params=params)
    json = r.json()
    data = json['data']

    return Image(url=data['image_url'])

def load_ipython_extension(ipython):
    ipython.register_magic_function(giphy, 'line')
