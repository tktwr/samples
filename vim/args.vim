"------------------------------------------------------
" args
"------------------------------------------------------
" *memo_vim.syntax.nargs*
func VimTestNargs(...)
  echom "nargs: ".a:0
  if a:0 == 1
    echom "a:1: ".a:1
  elseif a:0 == 2
    echom "a:1: ".a:1
    echom "a:2: ".a:2
  endif
endfunc

" *memo_vim.syntax.fargs*
func VimTestFargs(arg1, arg2)
  echom "VimTestFargs: [".a:arg1." ".a:arg2."]"
endfunc

" *memo_vim.syntax.qargs*
func VimTestQargs(arg)
  echom "VimTestQargs: [".a:arg."]"
endfunc

" *memo_vim.syntax.range*
func VimTestRange(arg1, arg2)
  echom "VimTestRange: [".a:arg1." ".a:arg2."]"
endfunc

func VimTestRange2() range
  echom "VimTestRange: [".a:firstline." ".a:lastline."]"
endfunc

"------------------------------------------------------
" command
"------------------------------------------------------
command -nargs=* VimTestNargs     call VimTestNargs(<f-args>)
command -nargs=+ VimTestFargs     call VimTestFargs(<f-args>)
command -nargs=+ VimTestQargs     call VimTestQargs(<q-args>)
command -range   VimTestRange     call VimTestRange(<line1>, <line2>)
command          VimTestRange2    '<,'>call VimTestRange2()

" replace the selected lines by the output
"vnoremap A :'<,'>!sumcol.py<CR>

" output to stdout
vnoremap A y:'<,'>w !sumcol.py<CR>

" pass the selected lines to a func
vnoremap C y:call VimTestQargs("<C-R>"")<CR>

