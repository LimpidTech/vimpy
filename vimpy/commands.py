# TODO: Consider making this functionality a decorator instead # of the
# __metaclass__ nightmare that it is.

import vim
import shlex
import inspect
from .util import AutoInstance

command_register_template = (
    'command '
    '{bang} '
    '{completion} '
    '-nargs={arg_count} '
    '{name} '
    'python vimpy_core_commands_call("{name}", "<args>")'
)

command_unregister_template = 'delcommand {name}'

def call_command(name, args):
    if name in global_command_map:
        varargs = shlex.split(args)

        # TODO: Allow other command maps
        command = global_command_map[name]

        try:
            command(*varargs)
        except TypeError, e:
            vim.command('echoerr {0}'.format(e.message))

class CommandMap(dict):
    def register(self, name, command):
        """ Register (apply to Vim) a command. """

        inspection = inspect.getargspec(command.run)

        arg_count = len(inspection.args) - 1

        # Provide support for argument expansion
        if inspection.varargs is not None:
            if arg_count > 0:
                arg_count = '+'
            else:
                arg_count = '*'

        # TODO: Support custom completions via Python functions.
        if getattr(command, 'completion', False) is not False:
            completion = '-complete={0}'.format(command.completion)
        else:
            completion = ''

        if getattr(command, 'bang', False):
            bang = '-bang'
        else:
            bang = ''

        context = {
            'name': name,
            'arg_count': arg_count,
            'completion': completion,
            'bang': bang
        }

        register_command = command_register_template.format(**context)

        # Register our command!
        vim.command(register_command)

    def deregister(self, name):
        """ Deregister any command managed by this map. """

        if name in self:
            vim.command(command_unregister_template.format(name=name))

            return True

        return False

    def __setitem__(self, key, value):
        if key in self:
            del self[key]

        self.register(key, value)
        super(CommandMap, self).__setitem__(key, value)

    def __delitem__(self, key):
        self.deregister(key)
        super(CommandMap, self).__delitem__(key)

# A default global command map
global_command_map = CommandMap()

class Command(object):
    """ A command which can be used inside Vim. """

    command_map = global_command_map
    __metaclass__ = AutoInstance

    completion = False
    bang = False

    def __init__(self, command_map=None, register=True):
        name = getattr(self, 'name', False)

        if name is False:
            self.name = self.__class__.__name__

        if register is True:
            self.register()

    def register(self):
        """ Registers the current command name with the Vim command map. """

        self.command_map[self.name] = self

    def __call__(self, *args, **kwargs):
        self.run(*args, **kwargs)

    def run(self):
        raise NotImplementedError('Can not call base VimpyCommand.')

# Wraps our commands in Python calls.
vim.command("python from vimpy.commands import call_command as vimpy_core_commands_call")

