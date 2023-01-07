"------------------------------------------------------
" popup term
"------------------------------------------------------
func! TestPopupCreateTerm()
  let cmd = [&shell]
  let term_opts = {
    \ 'hidden'      : 1,
    \ 'term_finish' : 'close',
    \ }
  let buf = term_start(cmd, term_opts)

  let win_opts = {
    \ 'border'    : [],
    \ 'minwidth'  : &columns/2,
    \ 'minheight' : &lines/2,
    \ }
  call popup_create(buf, win_opts)
endfunc

"------------------------------------------------------
" test
"------------------------------------------------------
func! Test()
  call TestPopupCreateTerm()
endfunc
