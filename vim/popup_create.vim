"------------------------------------------------------
" popup_create
"------------------------------------------------------
" *sample:vim.syntax.popup_create*
func! TestPopupCreate()
  let text = ['hello', 'world']
  let opts = {
    \ 'padding'     : [0,0,0,0],
    \ 'border'      : [1,1,1,1],
    \ 'borderchars' : ['─', '│', '─', '│', '╭', '╮', '╯', '╰'],
    \ }
  let s:popup_winid = popup_create(text, opts)
endfunc

" *sample:vim.syntax.popup_close*
func! TestPopupClose()
  call popup_close(s:popup_winid)
  unlet s:popup_winid
endfunc

"------------------------------------------------------
" test
"------------------------------------------------------
func! Test()
  if exists('s:popup_winid')
    call TestPopupClose()
  else
    call TestPopupCreate()
  endif
endfunc
