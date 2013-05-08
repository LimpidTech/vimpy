if !has('python')
  finish
endif

if exists("g:loaded_vimpy") || &cp
  finish
endif

let g:loaded_vimpy=1

if !exists("g:vimpy_ignored_modules")
	let g:vimpy_ignored_modules=""
endif

let s:vimpy_script_filename=expand("<sfile>")

python << EndPython

import sys
import os
import vim
import importlib

vimpy_script_filename = vim.eval('s:vimpy_script_filename')

vimpy_dir = os.path.abspath(os.path.dirname(os.path.dirname(vimpy_script_filename)))
docs_dir = os.path.join(vimpy_dir, 'docs')
bundle_dir = os.path.dirname(vimpy_dir)

pathogen_check = vim.eval('exists("g:loaded_pathogen")')
vundle_check = vim.eval('exists(":Bundle")')

if not pathogen_check and not vundle_check:
    message = open(os.path.join(docs_dir, 'pathogen_required.md'), 'r')

    vim.command("echo '{0}'".format(message.read()))
    message.close()

    # Quit from Vim. Someone installed this wrong.
    vim.command('finish')

else:
  vim.command('let g:vimpy_enabled = 1')
  ignored_modules = vim.eval('g:vimpy_ignored_modules').split(',')
  import_modules = []

# Loop through every app in our pathogen bundle, and expose it's
# plugin directory to Python.
  for filename in os.listdir(bundle_dir):
      if filename[0] == '.':
          continue

      abs_filename = os.path.join(bundle_dir, filename)

      if os.path.isdir(abs_filename):
          # TODO: Modify this to make real python names
          module_dirname = os.path.basename(abs_filename).lower()
          module_abspath = os.path.join(abs_filename, module_dirname)

          if os.path.isdir(module_abspath):
              sys.path = [abs_filename] + sys.path
              import_modules.append(module_dirname)

  for module in import_modules:
      if module not in ignored_modules:
          importlib.import_module(module)

EndPython

