"------------------------------------------------------
" popup_create
"------------------------------------------------------
" *memo_vim.syntax.popup_create*
func VimTestPopupCreate()
  let s:popup_winid = popup_create("hello world", {})
endfunc

" *memo_vim.syntax.popup_close*
func VimTestPopupClose()
  call popup_close(s:popup_winid)
endfunc

"------------------------------------------------------
" command
"------------------------------------------------------
command VimTestPopupCreate   call VimTestPopupCreate()
command VimTestPopupClose    call VimTestPopupClose()
command! PopupTerm call popup_create(term_start([&shell], #{ hidden: 1, term_finish: 'close'}), #{ border: [], minwidth: &columns/2, minheight: &lines/2 })
