import vim

command_register_template = 'command {name} python vimpy_core_commands_call("{name}")'
command_unregister_template = 'delcommand {name}'

def call_command(name):
    if name in command_map:
        command = command_map[name]
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

class Command(object):
    """ A command which can be used inside Vim. """

    def __init__(self, command_map=None, register=True):
        self.command_map = command_map
        name = getattr(self, 'name', False)

        if name is False:
            self.name = self.__class__.__name__

        if register is True:
            self.register()

    def register(self):
        """ Registers the current command name with the Vim command map. """

        command_map[self.name] = self

    def __call__(self, *args, **kwargs):
        self.run(*args, **kwargs)

    def run(self):
        raise NotImplementedError('Can not call base VimpyCommand.')

# A default global command map
command_map = CommandMap()

# Wraps our commands in Python calls.
vim.command("python from vimpy.commands import call_command as vimpy_core_commands_call")

