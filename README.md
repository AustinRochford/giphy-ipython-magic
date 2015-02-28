# giphy-ipython-magic

## Demo

![Demo](https://raw.githubusercontent.com/AustinRochford/giphy-ipython-magic/master/demo.gif)

## Installation

To install, do `pip install giphy-ipython-magic`.  The only dependencies are `IPython` and `requests`.

The magic can be loaded in two ways:

1. Execute `%load_ext giphy_magic`.  This must be run in every notebook where you want to use `%giphy`.
2. Add `'giphy_magic'` to `c.IPKernelApp.extensions` in your profile's `ipython_kernel_config.py` file.  This will cause the magic to be loaded into every notebook by default.

## Configuration

* The script attempts to read `$GIPHY_API_KEY` from the environment and defaults to the public beta key if that variable is not found.
* The constant `RANDOM_ON_NO_MATCH` controls what happens when Giphy cannot match the given tag.  If it is `False`, then a message is displayed.  If it is `True`, a random GIF is shown instead.
* The constant `MAX_RATING` controls the [rating](https://github.com/Giphy/GiphyAPI#parameters-4) of the GIF returned by Giphy.

## License and attribution

This software is distributed under the [MIT License](https://raw.githubusercontent.com/AustinRochford/giphy-ipython-magic/master/LICENSE).  If you can make money off of it, good for you!

![Powered by Giphy](https://raw.githubusercontent.com/AustinRochford/giphy-ipython-magic/master/powered_by_giphy.gif)
