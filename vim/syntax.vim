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
