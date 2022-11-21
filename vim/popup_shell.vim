"------------------------------------------------------
" shell
"------------------------------------------------------
let s:shell_out = ""

func MyCallback(channel, msg)
  echom 'MyCallback: ' . a:msg

  let s:shell_out = a:msg
endfunc

func MyGotOutput(channel, msg)
  echom 'MyGotOutput: ' . a:msg

  let msg = substitute(a:msg, '\r', '', 'g')
  if msg != ""
    let s:shell_out = msg
  endif
endfunc

func MyJobExit(job, status)
  echom 'MyJobExit: ' . s:shell_out
  echom 'job: ' . a:job
  echom 'status: ' . a:status

  "let line = ch_read(a:job)
  "echom 'ch_read' . line
endfunc

func MyCloseCb(channel)
  echom 'MyCloseCb: ' . s:shell_out

  "let line = ch_read(a:channel)
  "echom 'ch_read' . line
endfunc

func VimTestPopupCreateShellCmd()
	let buf = term_start(['fzy_bmk.sh', 'bmk_file.txt'], #{
		\ callback: function('MyCallback'),
		\ out_cb: function('MyGotOutput'),
		\ exit_cb: function('MyJobExit'),
		\ close_cb: function('MyCloseCb'),
    \ hidden: 1,
    \ term_finish: 'close'
    \ })
	let winid = popup_create(buf, #{minwidth: &columns/2, minheight: 12})
endfunc

