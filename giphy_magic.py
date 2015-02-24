from IPython.display import Image

import requests

API_ENDPOINT = 'http://api.giphy.com/v1/gifs/random'

# This is the Giphy API's public beta key, see https://github.com/Giphy/GiphyAPI
API_KEY = 'dc6zaTOxFJmzC'

RANDOM_ON_NO_MATCH = False

MAX_RATING = 'pg-13'

def get_params(tag):
    params = {'api_key': API_KEY}

    if tag is not None:
        params['tag'] = tag

    if MAX_RATING is not None:
        params['rating'] = MAX_RATING

    return params

def giphy(tag):
    params = get_params(tag)

    r = requests.get(API_ENDPOINT, params=params)
    json = r.json()
    data = json['data']

    if data and 'image_url' in data:
        return Image(url=data['image_url'])
    elif RANDOM_ON_NO_MATCH:
        return giphy(None)
    else:
        return 'Giphy could not match {}'.format(tag),

def load_ipython_extension(ipython):
    ipython.register_magic_function(giphy, 'line')
