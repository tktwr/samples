"------------------------------------------------------
" popup_dialog
"------------------------------------------------------
func VimTestPopupDialogHandler(id, result)
  echom a:result
  if a:result
    echom "yes"
  else
    echom "no"
  endif
endfunc

" *memo_vim.syntax.popup_dialog*
func VimTestPopupDialog()
  call popup_dialog('Continue? y/n', #{
    \ filter: 'popup_filter_yesno',
    \ callback: 'VimTestPopupDialogHandler',
    \ })
endfunc

command VimTestPopupDialog   call VimTestPopupDialog()
