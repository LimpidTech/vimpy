autocommands_map = {
    'pre_stdin_read': 'StdinReadPre',
    'post_buf_write': 'BufWritePost',
    'focus_lost': 'FocusLost',
    'cursor_moved_i': 'CursorMovedI',
    'pre_file_read': 'FileReadPre',
    'file_type': 'FileType',

# TODO: Implement Cmd-events, which require that these actions are taken by Python
# instead of Vim.
#    'buf_write_cmd': 'BufWriteCmd',

    'pre_buf_read': 'BufReadPre',
    'term_response': 'TermResponse',
    'buf_new_fil': 'BufNewFile',
    'buf_add': 'BufAdd',
    'buf_wipeout': 'BufWipeout',
    'insert_leave': 'InsertLeave',
    'file_changed_shell': 'FileChangedShell',
    'pre_vim_leave': 'VimLeavePre',
    'file_changed_ro': 'FileChangedRO',
    'buf_unload': 'BufUnload',
    'tab_enter': 'TabEnter',
    'tab_leave': 'TabLeave',
    'buf_hidden': 'BufHidden',
    'pre_buf_file': 'BufFilePre',
    'post_shell_filter': 'ShellFilterPost',
    'pre_buf_write': 'BufWritePre',
    'cmdwin_leave': 'CmdwinLeave',
    'buf_new': 'BufNew',
    'post_file_write': 'FileWritePost',
    'buf_create': 'BufCreate',
    'post_file_changed_shell': 'FileChangedShellPost',
    'guienter': 'GUIEnter',
    'insert_enter': 'InsertEnter',

# TODO: Implement Cmd-events, which require that these actions are taken by Python
# instead of Vim.
#    'source_cmd': 'SourceCmd',

    'post_file_read': 'FileReadPost',
    'buf_win_leave': 'BufWinLeave',
    'insert_change': 'InsertChange',
    'menu_popup': 'MenuPopup',
    'buf_leave': 'BufLeave',
    'win_enter': 'WinEnter',
    'post_file_append': 'FileAppendPost',
    'pre_source': 'SourcePre',
    'cursor_hold': 'CursorHold',
    'func_undefined': 'FuncUndefined',
    'spell_file_missing': 'SpellFileMissing',

# TODO: Implement Cmd-events, which require that these actions are taken by Python
# instead of Vim.
#    'pre_quick_fix_cmd': 'QuickFixCmdPre',

    'pre_filter_read': 'FilterReadPre',

# TODO: Implement Cmd-events, which require that these actions are taken by Python
# instead of Vim.
#    'post_shell_cmd': 'ShellCmdPost',
    'cursor_moved': 'CursorMoved',
    'post_session_load': 'SessionLoadPost',
    'pre_filter_write': 'FilterWritePre',
    'buf_delete': 'BufDelete',
    'buf_write': 'BufWrite',
    'vim_resized': 'VimResized',
    'user': 'User',
    'color_scheme': 'ColorScheme',
    'cmdwin_enter': 'CmdwinEnter',

# TODO: Implement Cmd-events, which require that these actions are taken by Python
# instead of Vim.
#    'file_append_cmd': 'FileAppendCmd',
#    'file_write_cmd': 'FileWriteCmd',

    'post_filter_read': 'FilterReadPost',

# TODO: Implement Cmd-events, which require that these actions are taken by Python
# instead of Vim.
#    'buf_read_cmd': 'BufReadCmd',

    'buf_enter': 'BufEnter',
    'focus_gained': 'FocusGained',

# TODO: Implement Cmd-events, which require that these actions are taken by Python
# instead of Vim.
#    'file_read_cmd': 'FileReadCmd',

    'pre_file_write': 'FileWritePre',
    'post_stdin_read': 'StdinReadPost',

    'syntax': 'Syntax',
    'cursor_hold_i': 'CursorHoldI',
    'vim_enter': 'VimEnter',
    'win_leave': 'WinLeave',
    'post_buf_read': 'BufReadPost',
    'remote_reply': 'RemoteReply',
    'post_buf_file': 'BufFilePost',

# TODO: Implement Cmd-events, which require that these actions are taken by Python
# instead of Vim.
#    'post_quick_fix_cmd': 'QuickFixCmdPost',

    'encoding_changed': 'EncodingChanged',
    'swap_exists': 'SwapExists',
    'pre_file_append': 'FileAppendPre',
    'buf_win_enter': 'BufWinEnter',
    'term_changed': 'TermChanged',
    'buf_read': 'BufRead',
    'post_filter_write': 'FilterWritePost',
    'vim_leave': 'VimLeave',
}
