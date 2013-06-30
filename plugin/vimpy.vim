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

import os,sys

# Bootstrap Python to include the vimpy_setup script.
vimpy_script_path = os.path.dirname(vim.eval('s:vimpy_script_filename'))
sys.path.append(vimpy_script_path)

# Now that we've appended it to our path, import vimpy_setup.
from vimpy_setup import Bootstrapper

# Now that we have a reference to `bootstrap`, remove it from our path
# before bootstrapping our modules.
sys.path.remove(vimpy_script_path)

# Bootstrap Vimpy modules.
Bootstrapper()

EndPython

