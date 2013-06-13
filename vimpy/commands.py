# TODO: Consider making this functionality a decorator instead
# of the __metaclass__ nightmare that it is.

import vim
from .util import AutoInstance

command_register_template = 'command {name} python vimpy_core_commands_call("{name}")'
command_unregister_template = 'delcommand {name}'

def call_command(name):
    if name in global_command_map:
        # TODO: Allow other command maps
        command = global_command_map[name]
        command()

class CommandMap(dict):
    def __setitem__(self, key, value):
        if key in self:
            del self[key]

        # Register our command!
        vim.command(command_register_template.format(name=key))

        super(CommandMap, self).__setitem__(key, value)

    def __delitem__(self, key):
        if key in self:
            vim.command(command_unregister_template.format(name=key))

        super(CommandMap, self).__delitem__(key)

# A default global command map
global_command_map = CommandMap()

class Command(object):
    """ A command which can be used inside Vim. """

    command_map = global_command_map
    __metaclass__ = AutoInstance

    def __init__(self, command_map=None, register=True):
        name = getattr(self, 'name', False)

        if name is False:
            self.name = self.__class__.__name__

        if register is True:
            self.register()

    def register(self):
        """ Registers the current command name with the Vim command map. """

        print(self.command_map)
        self.command_map[self.name] = self

    def __call__(self, *args, **kwargs):
        self.run(*args, **kwargs)

    def run(self):
        raise NotImplementedError('Can not call base VimpyCommand.')

# Wraps our commands in Python calls.
vim.command("python from vimpy.commands import call_command as vimpy_core_commands_call")

