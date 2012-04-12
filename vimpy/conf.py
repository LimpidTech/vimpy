import vim

vim_setter_command = 'let {0}="{1}"'

class VimpySettings(object):
    """ Provides a dict-like interface which can be used to access variables.
    
    Overrides __getitem__ and __setitem__ in order to allow developers to
    get and set the values of vimscript variables via a dict-like interface
    using the vimpy.settings['variable_name']

    """

    # TODO: Verify that the proper prefixes are working.

    def __getitem__(self, key):
        """ Returns the value of a variable. """

        return vim.eval(key)

    def __setitem__(self, key, value):
        """ Modifies the value of the provided variable. """

        # Attempt to escape provided values to be safely provided to vim
        final_value = str(value)
        final_value = final_value.replace('\\', '\\\\')
        final_value = final_value.replace('"', '\\"')

        vim.command(vim_setter_command.format(key, final_value))

settings = VimpySettings()

