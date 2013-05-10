import vim as vim_module

vim_setter_command = 'let {0}="{1}"'

class VariableWrapper(object):
    """ Provides a dict-like interface which can be used to access variables.
    
    Overrides __getitem__ and __setitem__ in order to allow developers to
    get and set the values of vimscript variables via a dict-like interface
    using the vimpy.settings['variable_name']

    """

    # TODO: Verify that the proper prefixes are working.
    def __init__(self, prefix=''):
       self.prefix = prefix

    def make_key(self, key):
        return '{0}{1}'.format(self.prefix, key)

    def __contains__(self, key):
        """ Allows us to check if a variable exists in this scope. """

        command = 'exists("{0}")'.format(self.make_key(key))
        return vim_module.eval(command) == '1'

    def __getitem__(self, key):
        """ Returns the value of a variable. """

        return vim_module.eval(self.make_key(key))

    def __setitem__(self, key, value):
        """ Modifies the value of the provided variable. """

        # Attempt to escape provided values to be safely provided to vim
        final_value = str(value)
        final_value = final_value.replace('\\', '\\\\')
        final_value = final_value.replace('"', '\\"')

        vim_module.command(vim_setter_command.format(self.make_key(key), final_value))

globals = VariableWrapper(prefix='g:')
window = VariableWrapper(prefix='w:')
tab = VariableWrapper(prefix='t:')
buffer = VariableWrapper(prefix='b:')
vim = VariableWrapper(prefix='v:')
options = VariableWrapper(prefix='&')
registers = VariableWrapper(prefix='@')
environment = VariableWrapper(prefix='$')

