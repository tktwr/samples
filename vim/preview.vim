function! ShowInPreview(name, fileType, lines)
  let l:command = "silent! pedit! +setlocal\\ " .
                \ "buftype=nofile\\ nobuflisted\\ " .
                \ "noswapfile\\ nonumber\\ " .
                \ "filetype=" . a:fileType . " " . a:name

  exe l:command

  if has('nvim')
    let l:bufNr = bufnr(a:name)
    call nvim_buf_set_lines(l:bufNr, 0, -1, 0, a:lines)
  else
    call setbufline(a:name, 1, a:lines)
  endif
endfunction

