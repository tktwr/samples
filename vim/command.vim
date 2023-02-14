func TestEdit(mods)
  exec a:mods 'new'
endfunc

command TestEdit call TestEdit(<q-mods>)

