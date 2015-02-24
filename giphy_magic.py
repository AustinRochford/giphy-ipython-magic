from IPython.display import Image

import requests

API_ENDPOINT = 'http://api.giphy.com/v1/gifs/random'

# This is the Giphy API's public beta key, see https://github.com/Giphy/GiphyAPI
API_KEY = 'dc6zaTOxFJmzC'

def giphy(tag):
    params = {
        'api_key': API_KEY,
        'tag': tag
    }

    r = requests.get(API_ENDPOINT, params=params)
    json = r.json()
    data = json['data']

    if data and 'image_url' in data:
        return Image(url=data['image_url'])
    else:
        return 'Giphy could not match {}'.format(tag)

def load_ipython_extension(ipython):
    ipython.register_magic_function(giphy, 'line')
