"------------------------------------------------------
" popup menu for vim
"------------------------------------------------------
func! TestPopupMenuFilter(id, key)
  echom printf("%d, %s", a:id, a:key)
  return popup_filter_menu(a:id, a:key)
endfunc

func! TestPopupMenuHandler(id, result)
  echom printf("%d, %d", a:id, a:result)
endfunc

func! TestPopupMenu_Vim81(title, list)
  let opts = {
    \ 'filter'      : 'TestPopupMenuFilter',
    \ 'callback'    : 'TestPopupMenuHandler',
    \ 'padding'     : [0,0,0,0],
    \ 'border'      : [1,1,1,1],
    \ 'borderchars' : ['─', '│', '─', '│', '╭', '╮', '╯', '╰'],
    \ 'pos'         : 'botleft',
    \ 'line'        : 'cursor-1',
    \ 'col'         : 'cursor',
    \ 'moved'       : 'WORD',
    \ }
  return popup_menu(a:list, opts)
endfunc

"------------------------------------------------------
" popup menu for nvim
"------------------------------------------------------
func! TestPopupMenuHandlerStr(str)
  echom printf("[%s]", a:str)
endfunc

" nvim with the plugin 'kamykn/popup-menu.nvim'
func! TestPopupMenu_Nvim(title, list)
  call popup_menu#open(a:list, function('TestPopupMenuHandlerStr'))
  return 0
endfunc

" nvim with the plugin 'Ajnasz/vim-popup-menu'
func! TestPopupMenu_Nvim2(title, list)
  let winid = popup_menu#open(a:list, function('TestPopupMenuHandlerStr'))
  set signcolumn=auto
  return winid
endfunc

"------------------------------------------------------
" popup menu for old vim / nvim
"------------------------------------------------------
func! TestPopupMenu_Input(title, list)
  let index = inputlist(a:list)
  call TestPopupMenuHandler(0, index)
  return 0
endfunc

"------------------------------------------------------
" test
"------------------------------------------------------
func! TestPopupMenu()
  let title = 'TestPopupMenu'
  let list = ['aaa', 'bbb', 'ccc']

  if exists('*popup_menu')
    let winid = TestPopupMenu_Vim81(title, list)
  elseif has('nvim') && exists('g:loaded_popup_menu_plugin')
    let winid = TestPopupMenu_Nvim(title, list)
  elseif has('nvim') && exists('g:loaded_popup_menu')
    let winid = TestPopupMenu_Nvim2(title, list)
  else
    let winid = TestPopupMenu_Input(title, list)
  endif
  return winid
endfunc

func! Test()
  call TestPopupMenu()
endfunc
