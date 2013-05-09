Vimpy
=====

Simply put, Vimpy allows you to write Vim plugins without writing any
Vimscript. This is done by abstracting Vim commands through a Pythonic
interface.

How does it use this?
------------------

Check out [the example plugin][ExamplePlugin] if
you'd like to see an implementation of a plugin using Vimpy. All you have to
do is define a python package in your project with a lowercase version of
the same name of the directory that your project's bundle is in, and Vimpy
will automatically import it.

For instance, with [the VimpyExample plugin][ExamplePlugin] you end up with a
module in VimplyExample called vimpyexample. It has a `plugin.py` (alongside
it's `__init__.py`, of course), which defines a class called
*VimpyExamplePlugin*.

Since the bundle is called VimpyExample, Vimpy will automatically perform
something similar to this at initialization of Vim:

    from vimpyexample.plugin import VimpyExamplePlugin

All autocommands can be defined inside of the VimpyExamplePlugin as object
methods with snake-case / Pythonic names. So, for instance - I could bind do
VimEnter like so:

    from vimpy.plugins import Plugin

    class VimplyExamplePlugin(Plugin):
        def vim_enter(self, data=None):
            print('Example VimEnter called.')

*Note: This is what [the VimpyExample plugin][ExamplePlugin] does.*

You can also access variables from Vim using a Pythonic interface. For
instance, you could do the following to see the key bound to mapleader
if you were inclined to do so:

    from vimpy import variables
    print(variables.globals['mapleader'])

or you could do this to see the current buffer's syntax setting:

    from vimpy import variables
    print(variables.buffer['current_syntax'])

Vimpy also makes setting variables just as simple:

    from vimpy import variables
    variables.globals['example_data'] = 'Okay!'
    

[ExamplePlugin]: https://github.com/LimpidTech/VimpyExample

