"""Greeter.

Usage:
 tested.py hello <name>...
 tested.py goodbye <name>
 tested.py (-h | --help)

Options:
 -h --help     Show this screen.

"""
from docopt import docopt


def hello(name):
   print('Hello, {0}'.format(name))


def goodbye(name):
   print('Goodbye, {0}'.format(name))

if __name__ == '__main__':
   arguments = docopt(__doc__)
   print(arguments['hello'])
