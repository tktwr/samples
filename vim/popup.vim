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

command! PopupTerm call popup_create(term_start([&shell], #{ hidden: 1, term_finish: 'close'}), #{ border: [], minwidth: &columns/2, minheight: &lines/2 })

"------------------------------------------------------
" shell
"------------------------------------------------------
let s:shell_out = ""

func MyCallback(channel, msg)
  echom 'MyCallback: ' . a:msg

  let s:shell_out = a:msg
endfunc

func MyGotOutput(channel, msg)
  "echom 'MyGotOutput: ' . a:msg

  let msg = substitute(a:msg, '\r', '', 'g')
  if msg != ""
    let s:shell_out = msg
  endif
endfunc

func MyJobExit(job, status)
  echom 'MyJobExit: ' . s:shell_out
  echom 'job, status: ' . a:job . ", " . a:status

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

"------------------------------------------------------
" popup_menu
"------------------------------------------------------
func VimTestPopupMenuFilter(id, key)
  " Handle shortcuts
  if a:key == 'S'
     call popup_close(a:id, 1)
     return 1
  endif
  if a:key == 'C'
     call popup_close(a:id, 2)
     return 1
  endif
  if a:key == 'D'
     call popup_close(a:id, 3)
     return 1
  endif

  " No shortcut, pass to generic filter
  return popup_filter_menu(a:id, a:key)
endfunc

func VimTestPopupMenuHandler(id, result)
  echo a:result
  if &buftype == 'terminal'
    let l:bufnr = winbufnr(0)
    "let l:cmd = "git status\<CR>"
    let l:cmd = "git status"
    call term_sendkeys(l:bufnr, l:cmd)
  endif
endfunc

" *memo_vim.syntax.popup_menu*
func VimTestPopupMenu()
  let cmd_list = ['Save', 'Cancel', 'Discard']
  call popup_menu(cmd_list, #{
    \ filter: 'VimTestPopupMenuFilter',
    \ callback: 'VimTestPopupMenuHandler',
    \ border: [0,0,0,0],
    \ padding: [0,0,0,0],
    \ pos: 'botleft',
    \ line: 'cursor-1',
    \ col: 'cursor',
    \ moved: 'WORD',
    \ })
endfunc

"------------------------------------------------------
" command
"------------------------------------------------------
command VimTestPopupCreate   call VimTestPopupCreate()
command VimTestPopupClose    call VimTestPopupClose()
command VimTestPopupDialog   call VimTestPopupDialog()
command VimTestPopupMenu     call VimTestPopupMenu()

