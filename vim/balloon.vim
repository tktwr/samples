"------------------------------------------------------
" balloon
"------------------------------------------------------
" *memo_vim.syntax.popup_beval*
func VimTestBalloonExpr()
  if s:winid && popup_getpos(s:winid) != {}
    " previous popup window still shows
    if v:beval_text == s:last_text
      " Still the same text, keep the existing popup
      return ''
    endif
    call popup_close(s:winid)
  endif
  let s:winid = popup_beval(v:beval_text, #{mousemoved: 'word'})
  let s:last_text = v:beval_text
  return ''
endfunc

" *memo_vim.syntax.balloon*
func VimTestBalloon()
  set ballooneval balloonevalterm
  set balloonexpr=VimTestBalloonExpr()
  let s:winid = 0
  let s:last_text = ''
endfunc

"------------------------------------------------------
command VimTestBalloon    call VimTestBalloon()
