" *memo_vim.syntax.autocmd*
"------------------------------------------------------
" test autocmd
"------------------------------------------------------
func VimTestEventMsg(msg)
  echo a:msg.": ".expand("%")
endfunc

func VimTestAutocmd()
  augroup ag_mytest
    autocmd!
    autocmd FileType txt     call VimTestEventMsg("FileType txt")
    autocmd FileType bmk     call VimTestEventMsg("FileType bmk")
    autocmd WinEnter *       call VimTestEventMsg("WinEnter")
    autocmd WinLeave *       call VimTestEventMsg("WinLeave")
    autocmd BufRead *        call VimTestEventMsg("BufRead")
    autocmd BufEnter *       call VimTestEventMsg("BufEnter")
    autocmd BufLeave *       call VimTestEventMsg("BufLeave")
    autocmd BufWinEnter *    call VimTestEventMsg("BufWinEnter")
    autocmd BufWinLeave *    call VimTestEventMsg("BufWinLeave")
  augroup END
endfunc

"------------------------------------------------------
" command
"------------------------------------------------------
command VimTestAutocmd       call VimTestAutocmd()

