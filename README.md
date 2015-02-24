# giphy-ipython-magic

## Demo

![Demo](https://raw.githubusercontent.com/AustinRochford/giphy-ipython-magic/master/demo.gif)

## Installation

To use this magic, put `giphy_magic.py` on your `PYTHONPATH` and add `'giphy_magic'` to `c.IPKernelApp.extensions` in your `ipython_notebook_config.py`.

## Configuration

* If you have recieved a private Giphy API key, you can replace the public beta key in `API_KEY`.
* The constant `RANDOM_ON_NO_MATCH` controls what happens when Giphy cannot match the given tag.  If it is `False`, then a message is displayed.  If it is `True`, a random GIF is shown instead.
* The constant `MAX_RATING` controls the [rating](https://github.com/Giphy/GiphyAPI#parameters-4) of the GIF returned by Giphy.

## License and attribution

This software is distributed under the [MIT License](https://raw.githubusercontent.com/AustinRochford/giphy-ipython-magic/master/LICENSE).  If you can make money off of it, good for you!

![Powered by Giphy](https://raw.githubusercontent.com/AustinRochford/giphy-ipython-magic/master/powered_by_giphy.gif)
