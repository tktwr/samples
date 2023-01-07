func! TestStrLen()
  "let separator = "=============================="
  let separator = "══════════════════════════════"
  "let separator = "──────────────────────────────"

  echom printf('strlen          : %s', strlen(separator))
  echom printf('strchars        : %s', strchars(separator))
  echom printf('strdisplaywidth : %s', strdisplaywidth(separator))
  echom printf('strwidth        : %s', strwidth(separator))

  " no func in nvim
  echom printf('strcharlen      : %s', strcharlen(separator))
endfunc

func! TestNerdFont()
  echo "> [\u2b80]"
  echo "< [\u2b82]"
  echo "> [\uf44a]"
  echo "> [\ue0b0]"
  echo "> [\ue0b1]"
  echo "< [\ue0b2]"
  echo "< [\ue0b3]"
  echo "  [\ue0b4]"
  echo "  [\ue0b6]"
  echo "  [\ue0b8]"
  echo "  [\ue0ba]"
  echo "  [\ue0d2]"
  echo "  [\ue0d2]"
  echo "  [\ue0d4]"
  echo "  [\ue0c6]"
  echo "  [\ue0c0]"
  echo "  [\uf5b5]"
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
endfunc
