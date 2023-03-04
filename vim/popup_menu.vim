"------------------------------------------------------
" popup_menu
"------------------------------------------------------
func! TestPopupMenuFilter(id, key)
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

func! TestPopupMenuHandler(id, result)
  echo a:result
  if &buftype == 'terminal'
    let l:bufnr = winbufnr(0)
    "let l:cmd = "git status\<CR>"
    let l:cmd = "git status"
    call term_sendkeys(l:bufnr, l:cmd)
  endif
endfunc

" *sample_vim.syntax.popup_menu*
func! TestPopupMenu()
  let cmd_list = ['Save', 'Cancel', 'Discard']
  let opts = {
    \ 'filter'      : 'TestPopupMenuFilter',
    \ 'callback'    : 'TestPopupMenuHandler',
    \ 'padding'     : [0,0,0,0],
    \ 'border'      : [1,1,1,1],
    \ 'borderchars' : ['─', '│', '─', '│', '╭', '╮', '╯', '╰'],
    \ 'pos'         : 'botleft',
    \ 'line'        : 'cursor-1',
    \ 'col'         : 'cursor',
    \ 'moved'       : 'WORD',
    \ }
  call popup_menu(cmd_list, opts)
endfunc

"------------------------------------------------------
" test
"------------------------------------------------------
func! Test()
  call TestPopupMenu()
endfunc
