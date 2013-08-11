import vim
import re


class State(object):
    tabpage = vim.current.tabpage
    window = vim.current.window
    buffer = vim.current.buffer
    range = vim.current.range
    line = vim.current.line

    def get_word(self):
        return vim.bindeval('expand("<cword>")')

    def set_word(self, word):
        vim.command('normal ciw{0}'.format(word))

    def del_word(self):
        vim.command('normal cw')

    word = property(
        get_word,
        set_word,
        del_word,

        'Word currently under the cursor.'
    )


current = State()
