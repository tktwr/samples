"------------------------------------------------------
" popup_dialog
"------------------------------------------------------
func! TestPopupDialogHandler(id, result)
  echom a:result
  if a:result
    echom "yes"
  else
    echom "no"
  endif
endfunc

" *memo_vim.syntax.popup_dialog*
func! TestPopupDialog()
  let text = split(&runtimepath, ',')
  let text += ['Continue? y/n']
  let opts = {
    \ 'filter'      : 'popup_filter_yesno',
    \ 'callback'    : 'TestPopupDialogHandler',
    \ 'padding'     : [0,0,0,0],
    \ 'border'      : [1,1,1,1],
    \ 'borderchars' : ['─', '│', '─', '│', '╭', '╮', '╯', '╰'],
    \ 'minwidth'    : &columns/2,
    \ 'maxheight'   : 20,
    \ }
  call popup_dialog(text, opts)
endfunc

"------------------------------------------------------
" test
"------------------------------------------------------
func! Test()
  call TestPopupDialog()
endfunc
