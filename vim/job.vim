" *sample_vim.syntax.job_start*
"------------------------------------------------------
" job
"------------------------------------------------------
func VimTestJobCloseHandler(channel)
  let text = ""
  let i = 1
  while ch_status(a:channel, {'part': 'out'}) == 'buffered'
    let text = ch_read(a:channel)
    call setline(i, text)
    let i = i + 1
  endwhile
endfunc

" *sample_vim.syntax.job_start*
func VimTestJobStartAndClose()
  let cmd = "ls -l"
  let s:job = job_start(cmd, {"close_cb": "VimTestJobCloseHandler"})
endfunc

"------------------------------------------------------
" job
"------------------------------------------------------
func VimTestHello()
  let i = 1
  while i <= 20
    let text = "hello " . i
    call setline(i, text)
    redraw
    sleep 1
    let i = i + 1
  endwhile
endfunc

func VimTestJobHandler(channel, msg)
  call setline(1, a:msg)
endfunc

func VimTestJobStart()
  let s:job = job_start("hello", {"callback": "VimTestJobHandler"})
  "let s:job = job_start("VimTestHello", {"callback": "VimTestJobHandler"})
endfunc

func VimTestJobStop()
  call job_stop(s:job)
endfunc

func VimTestJobStatus()
  echom job_status(s:job)
endfunc

"------------------------------------------------------
" command
"------------------------------------------------------
command VimTestJobStartAndClose call VimTestJobStartAndClose()

command VimTestJobStart         call VimTestJobStart()
command VimTestJobStop          call VimTestJobStop()
command VimTestJobStatus        call VimTestJobStatus()

