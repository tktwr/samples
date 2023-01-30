func! TestList()
  let l = [0, 1, 2]
  echom l
  echom l[0:]
  echom l[0:1]
endfunc

func! TestDict()
  let d = {'aaa': 111, 'bbb': 222}
  echom d['aaa']
  echom get(d, 'ccc', '000')
  let d['ddd'] = 333
  echom d['ddd']
endfunc

func! TestMatch()
  let s = 'ft:fugitive'
  echom match(s, '^ft:')
  echom match(s, '^syn:')
endfunc

func! TestSubstr()
  let i = 12
  let fname = "/a/b/c/d.txt"
  let str = printf("%3d %s ", i, fname)
  let substr = str[4:-2]
  let nr = str2nr(str[0:2])

  echom printf('str: [%s]', str)
  echom printf('nr: [%d]', nr)
  echom printf('substr: [%s]', substr)
  echom str == fname
  echom substr == fname
endfunc

func! GetItem(line, idx)
  let mx = '[-+*] \(.\+\)\s*|\s*\(.\+\)\s*$'
  let line = a:line
  let line = matchstr(line, mx)
  let item = substitute(line, mx, '\'.a:idx, '')
  let item = substitute(item, '\s*$', '', '')
  return item
endfunc

func! TestGetItem()
  let s = '- V  ViewThis          (C-CR)         | :call bmk#ViewThis()   '
  echom printf('item 0: [%s]', GetItem(s, 0))
  echom printf('item 1: [%s]', GetItem(s, 1))
  echom printf('item 2: [%s]', GetItem(s, 2))
endfunc

func! FormatKey(line, max_len)
  if match(a:line, '(.\+)') == -1
    let key = a:line
    let nspaces = a:max_len - strchars(key)
    let fmt = printf('%%s%%%ds', nspaces)
    return printf(fmt, key, ' ')
  else
    let mx = '\(.\+\)\((.\+)\)'
    let line = a:line
    let line = matchstr(line, mx)
    let key = substitute(line, mx, '\1', '')
    let key = substitute(key, '\s*$', '', '')
    let map = substitute(line, mx, '\2', '')
    let nspaces = a:max_len - strchars(key)
    let chars = strchars(map)
    if nspaces > chars
      let fmt = printf('%%s%%%ds', nspaces)
    else
      let fmt = printf('%%s %%s')
    endif
    return printf(fmt, key, map)
  endif
endfunc

func! TestFormatKey()
  echom printf('[%-30s]', ' ')
  let s = 'V  ViewThis hello world hello world    (C-CR)'
  echom printf('[%s]', FormatKey(s, 30))
  let s = 'V  ViewThis          (C-CR)'
  echom printf('[%s]', FormatKey(s, 30))
  let s = 'V  ViewThis'
  echom printf('[%s]', FormatKey(s, 30))
endfunc

func! TestLen()
  let s = ' ViewThis'
  echom printf('len: %d', len(s))
  echom printf('strlen: %d', strlen(s))
  echom printf('strlen: %d', strchars(s))
endfunc

"------------------------------------------------------
" test
"------------------------------------------------------
func! Test()
  "call TestList()
  "call TestDict()
  "call TestMatch()
  "call TestSubstr()
  "call TestGetItem()
  call TestFormatKey()
  "call TestLen()
endfunc
