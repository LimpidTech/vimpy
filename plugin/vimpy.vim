if exists("g:loaded_vimpy") || &cp
  finish
endif

let g:loaded_vimpy=1
let s:vimpy_script_filename=expand("<sfile>")

python << EOF
import sys
import os
import vim
import importlib

vimpy_script_filename = vim.eval('s:vimpy_script_filename')

# Get our different directories
vimpy_dir = os.path.abspath(os.path.dirname(os.path.dirname(vimpy_script_filename)))
docs_dir = os.path.join(vimpy_dir, 'docs')
bundle_dir = os.path.dirname(vimpy_dir)

# Make sure that the user is using pathogen before continuing
pathogen_check = vim.eval('g:loaded_pathogen')

if not pathogen_check:
    message = open(os.path.join(docs_dir, 'pathogen_required.md'), 'r')
    print("{0}\n".format(message.read()))
    message.close()

    # Quit from Vim. Someone installed this wrong.
    vim.command('quit')

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
            importlib.import_module(module_dirname)
            sys.path = sys.path[1:]
EOF

