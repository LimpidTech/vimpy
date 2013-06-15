import os

file_path = os.path.dirname(__file__)


class AutoInstance(type):
    def __new__(mcs, name, bases, dict):
        new_type = type.__new__(mcs, name, bases, dict)

        if getattr(new_type, 'auto_instance', True):
            new_type()

        return new_type


def template(filename):
    """ Returns the data from the provided template filename. """

    handle = open(os.sep.join([
        file_path,
        'templates',
        filename + '.vim'
    ]), 'r')

    return handle.read()
