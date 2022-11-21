"------------------------------------------------------
" shell
"------------------------------------------------------
let s:shell_out = ""

func PopupShellOutputCb(channel, msg)
  let msg = substitute(a:msg, '\r', '', 'g')
  if msg != ""
    let s:shell_out = msg
  endif
endfunc

func PopupShellCloseCb(channel)
  echom 'PopupShellCloseCb: ' . s:shell_out
endfunc

func PopupShell()
  let cmd = 'fzy_bmk.sh'
  let bmk = 'bmk_file.txt'
	let buf = term_start([cmd, bmk], #{
		\ out_cb: function('PopupShellOutputCb'),
		\ close_cb: function('PopupShellCloseCb'),
    \ hidden: 1,
    \ term_finish: 'close'
    \ })
	let winid = popup_create(buf, #{
    \ title: printf(" [fzy: %s] ", bmk),
    \ border: [],
    \ minwidth: &columns/2,
    \ minheight: 12
    \ })
endfunc

