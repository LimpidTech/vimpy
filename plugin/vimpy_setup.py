import os
import sys
import vim
import importlib


class Bootstrapper(object):
    packages = []

    modules = [
        'commands',
        'plugin',
    ]

    def __init__(self, *args, **kwargs):
        """ Wrap bootstrap as a callable. """

        self.bootstrap(*args, **kwargs)

    def get_ignored_modules(self):
        """ Update the ignored modules list. """

        # Get the ignored modules setting as a string.
        ignored_modules = vim.bindeval('g:vimpy_ignored_modules')
        ignored_modules = ignored_modules.split(',')

        # Remove all empty items from resulting list.
        return filter(None, ignored_modules)

    def get_runtime_paths(selfself):
        """ Gets Vim's runtime paths as a list. """

        paths = vim.bindeval('&rtp')
        return paths.split(',')

    def get_module_paths(self):
        """ Iterates runtime paths and adds any Python modules to the list. """

        module_paths = []

        for plugin_path in self.get_runtime_paths():
            if not os.path.isdir(plugin_path):
                continue

            file_names = os.listdir(plugin_path)

            # This is a pure-Python plugin!
            if '__init__.py' in file_names:
                module_paths.append(plugin_path)
                continue

            # Soon-to-be-deprecated support for the old organizational
            # structure.
            plugin_name = plugin_path.split(os.sep)[-1]

            if plugin_name.lower() in file_names:
                module_paths.append(os.sep.join([
                    plugin_path, plugin_name.lower()
                ]))

        return module_paths

    def setup_modules(self):
        """ Setup module paths. """

        module_paths = self.get_module_paths()

        for path in module_paths:
            module_path = os.path.dirname(path)
            module_name = path[len(module_path)+1:]

            if module_path not in sys.path:
                sys.path.append(module_path)

            self.packages.append(module_name)

    def initialize_modules(self):
        """ Initialize Vimpy modules. """

        ignored_modules = self.get_ignored_modules()

        for package_name in self.packages:
            for module_name in self.modules:
                if module_name in ignored_modules:
                    continue

                module_string = package_name + '.' + module_name

                try:
                    importlib.import_module(module_string)
                except ImportError:
                    pass

    def bootstrap(self):
        """ Bootstraps Vimpy. """

        self.setup_modules()
        self.initialize_modules()
