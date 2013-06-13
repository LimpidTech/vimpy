Vimpy
=====

Simply put, Vimpy allows you to write Vim plugins without writing any
Vimscript. This is done by abstracting Vim commands through a Pythonic
interface.

Documentation
-------------

[Vimpy's documentation][wiki] is available at the [GitHub wiki page][wiki]. If
you run into any problems with the documentation, or if you just have a
recommendation on how to make it better - please don't hesitate to [create a
new issue][issue]. We expect that Vimpy might have a couple issues, and will
always want to make this library better in any way possible.

Quick Start
------------------

Check out [the example plugin][ExamplePlugin] if you'd like to see an
implementation of a plugin using Vimpy. All you have to do is define a python
package in your project with a lowercase version of the same name of the
directory that your project's bundle is in, and Vimpy will automatically import
it.

For instance, with [the VimpyExample plugin][ExamplePlugin] you end up with a
module in VimplyExample called vimpyexample. It has a `plugin.py` (alongside
it's `__init__.py`, of course), which defines a class called
*VimpyExamplePlugin*.

When Vim is initialized, Vimpy will automatically perform the following:

    import vimpyexample

All autocommands can be defined inside of the VimpyExamplePlugin as object
methods with snake-case / Pythonic names. So, for instance - I could bind to
VimEnter like so:

    import vimpy

    class VimplyExamplePlugin(vimpy.Plugin):
        def vim_enter(self, data=None):
            print('Example VimEnter called.')

*Note: This is what [the VimpyExample plugin][ExamplePlugin] does.*

Vimpy observes the Plugin class, so all this package needs to do is
instantiate a plugin object for it to start receiving autocommand events.
If you'd prefer that your plugin doesn't automatically register for these
events, you can define a Plugin like so:

    from vimpy.plugins import Plugin

    class MyPlugin(Plugin):
        auto_register = False

Vimpy also exposes Vim's variables using a more Pythonic interface. For
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

This allows you to change many Vim options - as well as options for
plugins which don't provide a Pythonic interface. Other plugins can
access these variables just as you would expect. For instance, you
could check the value of the variable that we just set by simply
executing `:echo g:example_data` from Vim's command mode.


[ExamplePlugin]: https://github.com/LimpidTech/VimpyExample
[wiki]: https://github.com/LimpidTech/Vimpy/wiki
[issue]: https://github.com/LimpidTech/Vimpy/issues/new

