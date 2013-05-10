import vim as vim_module

stop_iter_message = 'Done iterating {0} variables.'

class VariableWrapper(object):
    """ Provides a dict-like interface which can be used to access variables.
    
    Overrides __getitem__ and __setitem__ in order to allow developers to
    get and set the values of vimscript variables via a dict-like interface
    using the vimpy.settings['variable_name']

    """

    def __init__(self, prefix=''):
       self.prefix = prefix

    def make_name(self, key):
        return '{0}{1}'.format(self.prefix, key)

    def keys(self):
        if not self.prefix in ['g:', 'v:', '']:
            return vim_module.bindeval(self.prefix).keys()
        else:
            return vim_module.vars.keys()

    def iterkeys(self):
        keys = self.keys()

        for key in keys:
            yield key

        raise StopIteration(stop_iter_message.format(self.prefix))

    def iteritems(self):
        def iteritems_generator():
            for key in self:
                yield key, self[key]

            raise StopIteration(stop_iter_message.format(self.prefix))

        return iteritems_generator()

    def itervalues(self):
        def itervalues_generator():
            for key in self:
                yield self[key]
            
            raise StopIteration(stop_iter_message.format(self.prefix))

        return itervalues_generator()

    def values(self):
        return list(self.itervalues())

    def remove(self, key):
        del self[key]

    def clear(self):
        for key in self.keys():
            self.remove(key)

    def pop(self, key):
        value = vim_module.bindeval(format(self.make_name(key)))

        self.remove(key)

        return value

    def popitem(self):
        key = self.iterkeys().next()

        return key, self.pop(key)

    def copy(self):
        result = {}

        for key, value in self.iteritems():
            result[key] = value

        return result

    def update(self, basis):
        for key in basis:
            self[key] = basis[key]

    def setdefault(self, key, value=None):
        if key in self:
            return self[key]

        self[key] = value

        return value

    def __len__(self):
        return len(self.keys())

    def __getitem__(self, key):
        """ Returns the value of a variable. """

        return vim_module.eval(self.make_name(key))

    def __setitem__(self, key, value):
        """ Modifies the value of the provided variable. """

        # Attempt to escape provided values to be safely provided to vim
        final_value = str(value)
        final_value = final_value.replace('\\', '\\\\')
        final_value = final_value.replace('"', '\\"')

        variable = self.make_name(key)

        command = 'islocked("{0}")'.format(variable)
        is_locked = vim_module.eval(command)

        if int(is_locked) > 0:
            raise TypeError('Tried to alter {0} but it is locked.'.format(variable))

        command = 'let {0}="{1}"'.format(self.make_name(key), final_value)
        return vim_module.command(command)

    def __delitem__(self, key):
        vim_module.command('unlet {0}'.format(self.make_name(key)))

    def __contains__(self, key):
        """ Allows us to check if a variable exists in this scope. """

        command = 'exists("{0}")'.format(self.make_name(key))
        return vim_module.eval(command) == '1'

    def __iter__(self):
        keys = self.keys()

        for key in keys:
            yield key

        raise StopIteration(stop_iter_message.format(self.prefix))

globals = VariableWrapper(prefix='g:')
window = VariableWrapper(prefix='w:')
tab = VariableWrapper(prefix='t:')
buffer = VariableWrapper(prefix='b:')
vim = VariableWrapper(prefix='v:')
options = VariableWrapper(prefix='&')
registers = VariableWrapper(prefix='@')
environment = VariableWrapper(prefix='$')

