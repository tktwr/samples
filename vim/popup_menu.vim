"------------------------------------------------------
" popup_menu
"------------------------------------------------------
func VimTestPopupMenuFilter(id, key)
  " Handle shortcuts
  if a:key == 'S'
     call popup_close(a:id, 1)
     return 1
  endif
  if a:key == 'C'
     call popup_close(a:id, 2)
     return 1
  endif
  if a:key == 'D'
     call popup_close(a:id, 3)
     return 1
  endif

  " No shortcut, pass to generic filter
  return popup_filter_menu(a:id, a:key)
endfunc

func VimTestPopupMenuHandler(id, result)
  echo a:result
  if &buftype == 'terminal'
    let l:bufnr = winbufnr(0)
    "let l:cmd = "git status\<CR>"
    let l:cmd = "git status"
    call term_sendkeys(l:bufnr, l:cmd)
  endif
endfunc

" *memo_vim.syntax.popup_menu*
func VimTestPopupMenu()
  let cmd_list = ['Save', 'Cancel', 'Discard']
  call popup_menu(cmd_list, #{
    \ filter: 'VimTestPopupMenuFilter',
    \ callback: 'VimTestPopupMenuHandler',
    \ border: [0,0,0,0],
    \ padding: [0,0,0,0],
    \ pos: 'botleft',
    \ line: 'cursor-1',
    \ col: 'cursor',
    \ moved: 'WORD',
    \ })
endfunc

command VimTestPopupMenu     call VimTestPopupMenu()