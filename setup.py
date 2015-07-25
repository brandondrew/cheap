from distutils.core import setup
import os

setup(
    name         = 'cheap',
    version      = '2.1.10',
    author       = 'Brandon Zylstra',
    author_email = 'first.last@gmail.com',
    license      = 'GPL3',
    description  = 'cheap allows you to create and view interactive cheatsheets '
    'on the command-line without conflicts with the original cheat by defunkt. '
    'It was designed to help remind *nix system administrators of options for'
    'commands that they use frequently, but not frequently enough to remember.',
    url          = 'https://github.com/brandondrew/cheap',
    packages     = [
        'cheap',
        'cheap.cheatsheets',
        'cheap.test',
    ],
    package_data = {
        'cheap.cheatsheets': [f for f in os.listdir('cheap/cheatsheets') if '.' not in f]
    },
    scripts          = ['bin/cheap'],
    install_requires = [
        'docopt >= 0.6.1',
        'pygments >= 1.6.0',
    ]
)
