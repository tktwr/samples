func VimTestSyntax(name)
  echom '---'

  echom a:name == ''

  let s = 'ft:fugitive'
  echom match(s, '^ft:')

  let d = {'aaa': 111, 'bbb': 222}
  echom d['aaa']
  echom get(d, 'ccc')
  let d['ddd'] = 333
  echom d['ddd']
endfunc
