import vim
from .autocommands import autocommands_map

# TODO: Make this more cleanly
observers = []

def call_observers(event_name):
    for observer in observers:
        observer.emit(event_name)

vim.command("python from vimpy.plugins import call_observers")

for command in autocommands_map:
    # Automating Cmd-Events is bad news. These must instead
    # be bound manually by the plugin.
    if autocommands_map[command][-3:] == 'Cmd':
        continue

    au_command = 'autocmd {0} * :python call_observers("{0}");'.format(autocommands_map[command])
    vim.command(au_command)

class PluginObserver(object):
    """ Provides a centralized observer for propagating Vim autocommands.

    Directly listens to Vim events and propagates them as required through
    any event listeners that register themselves with this object and provide
    the proper hooking methods.

    """

    def __init__(self):
        """ Initializes a dict of events and their related listeners list.
        
        Initializes self.listeners as a dict where keys are method names that
        are intended to respond to events. Each value is set to an empty list
        which contains all objects which are triggered by this event.

        """

        self.emitters = {}
        self.listeners = {}

        for event in autocommands_map:
            self.listeners[event] = []

        observers.append(self)

    def create_emitter(self, event_name):
        """ Returns an emitter that will trigger event_name on listeners. """

        handler_name_found = None

        for handler_name in autocommands_map:
            if autocommands_map[handler_name] == event_name:
                handler_name_found = handler_name
                break

        if not handler_name_found:
            raise NotImplementedError('No event handler exists for: {0}'.format(event_name))

        # Create the inner function. This functionally allows us to completely
        # fire events without doing any lookups in order to be as fast as
        # possible and prevent our process from blocking Vim.
        def emitter(context, data=None):
            if handler_name in context.listeners:
                for listener in context.listeners[handler_name]:
                    handler = getattr(listener, handler_name)
                    handler(data)

        return emitter

    def emit(self, event_name):
        """ Creates a new emitter if this is a new event. Fires the event. """

        if event_name not in self.emitters:
            self.emitters[event_name] = self.create_emitter(event_name)

        emitter = self.emitters[event_name]

        # TODO: We need to look into emitting data along with the event.
        emitter(self)

    def register(self, listener):
        """ Registers any event handlers within the given object

        """

        for event in autocommands_map:
            if getattr(listener, event, False):
                if not listener in self.listeners[event]:
                    self.listeners[event].append(listener)

class Plugin(object):
    """ Provides Pythonic event handling as an abstraction of Vim's events. """

    auto_register = True

    def __init__(self, observer=None): 
        """ Sets up our plugin observer and registers to it if necessary. """

        if observer is None:
            observer = default_observer

        # Automatically register this object with the observer if necessary.
        if self.auto_register is True:
            observer.register(self)

# Instantiate a default observer for plugins that don't provide it explicitly
default_observer = PluginObserver()

