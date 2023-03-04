" *sample:vim.syntax.autocmd*
"------------------------------------------------------
" test autocmd
"------------------------------------------------------
func! TestEventMsg(msg)
  echom a:msg.": ".expand("%")
endfunc

func! TestAutocmd()
  augroup ag_mytest
    autocmd!
    autocmd FileType txt     call TestEventMsg("FileType txt")
    autocmd FileType bmk     call TestEventMsg("FileType bmk")
    autocmd WinEnter *       call TestEventMsg("WinEnter")
    autocmd WinLeave *       call TestEventMsg("WinLeave")
    autocmd BufRead *        call TestEventMsg("BufRead")
    autocmd BufEnter *       call TestEventMsg("BufEnter")
    autocmd BufLeave *       call TestEventMsg("BufLeave")
    autocmd BufWinEnter *    call TestEventMsg("BufWinEnter")
    autocmd BufWinLeave *    call TestEventMsg("BufWinLeave")
  augroup END
endfunc

"------------------------------------------------------
" test
"------------------------------------------------------
func! Test()
  call TestAutocmd()
endfunc
