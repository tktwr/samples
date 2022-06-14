func VimTestSyntax(name)
  echom '---'

  let l = [0, 1, 2]
  echom l
  echom l[0:]
  echom l[0:1]

  echom a:name == ''

  let s = 'ft:fugitive'
  echom match(s, '^ft:')

  let d = {'aaa': 111, 'bbb': 222}
  echom d['aaa']
  echom get(d, 'ccc')
  let d['ddd'] = 333
  echom d['ddd']
endfunc

func VimTestString()
  let i = 12
  let fname = "/a/b/c/d.txt"
  let str = printf("%3d %s ", i, fname)
  let substr = str[4:-2]
  let nr = str2nr(str[0:2])

  echom "nr = [".nr."]"
  echom "str = [".str."]"
  echom "substr = [".substr."]"
  echom str == fname
  echom substr == fname
endfunc

