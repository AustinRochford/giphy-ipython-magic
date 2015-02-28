try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='giphy-ipython-magic',
    version='0.0.2',
    author="Austin Rochford",
    author_email="austin.rochford@gmail.com",
    description="giphy line magic for ipython 2 and 3",
    install_requires=['ipython>=2.0', 'requests'],
    keywords="ipython",
    license="MIT",
    long_description="""This package provides a line magic for embedding random GIFs from giphy.com in IPython notebooks""",
    platforms='any',
    py_modules=['giphy_magic'],
    url="https://github.com/AustinRochford/giphy-ipython-magic",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ]
)
