func! TestStrLen()
  "let separator = "=============================="
  "let separator = "══════════════════════════════"
  "let separator = "──────────────────────────────"
  let separator = "	──────────────────────────────"

  echom printf('strlen          : %s', strlen(separator))
  echom printf('strchars        : %s', strchars(separator))
  echom printf('strdisplaywidth : %s', strdisplaywidth(separator))
  echom printf('strwidth        : %s', strwidth(separator))

  if !has('nvim')
    echom printf('strcharlen      : %s', strcharlen(separator))
  endif
endfunc

func! TestNerdFont()
  echo "> [\ue0b0]"
  echo "> [\ue0b1]"
  echo "< [\ue0b2]"
  echo "< [\ue0b3]"
  echo "┌─────┐"
  echo "│     │"
  echo "└─────┘"
  echo ""
  echo ""
  echo ""
  echo "  "
  echo "  "
  echo "  "
  echo "  "
  echo "  "
  echo "  "
endfunc

func! Test()
  call TestStrLen()
  "call TestNerdFont()
endfunc
