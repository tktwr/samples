"------------------------------------------------------
" popup shell
"------------------------------------------------------
let s:shell_out = ""

func OutCb(channel, msg)
  let s:shell_out = a:msg
endfunc

func CloseCb(channel)
  let s:shell_out = substitute(s:shell_out, '\r', '', 'g')
  echom 'CloseCb: ' . s:shell_out
endfunc

func! TestPopupCreateShellCmd()
  let cmd = ['fzy_bmk.sh', 'bmk_file.txt']
	let term_opts = {
		\ 'out_cb'      : function('OutCb'),
		\ 'close_cb'    : function('CloseCb'),
    \ 'hidden'      : 1,
    \ 'term_finish' : 'close'
    \ }
	let buf = term_start(cmd, term_opts)

	let win_opts = {
    \ 'title'       : printf(" [%s] ", join(cmd)),
    \ 'border'      : [1,1,1,1],
    \ 'borderchars' : ['─', '│', '─', '│', '╭', '╮', '╯', '╰'],
    \ 'minwidth'    : &columns/2,
    \ 'minheight'   : 12
    \ }
	let winid = popup_create(buf, win_opts)
endfunc

"------------------------------------------------------
" test
"------------------------------------------------------
func! Test()
  call TestPopupCreateShellCmd()
endfunc
