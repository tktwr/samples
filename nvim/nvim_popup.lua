require('plenary.reload').reload_module('popup')
local popup = require('popup')

local lst = {
  "option  1",
  "option  2",
  "option  3",
  "option  4",
  "option  5",
  "option  6",
  "option  7",
  "option  8",
  "option  9",
  "option 10",
  "option 11",
  "option 12",
  "option 13",
  "option 14",
  "option 15",
  "option 16",
  "option 17",
  "option 18",
  "option 19",
  "option 20",
}
local cb = function(win_id, sel) print(sel) end

popup.create(lst, {
  title = "test",
  line = "cursor+2",
  col = "cursor+2",
  border = {1, 1, 1, 1},
  borderchars = {'─', '│', '─', '│', '╭', '╮', '╯', '╰'},
  enter = true,
  cursorline = true,
  callback = cb,
})
