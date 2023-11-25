import curses as cur

msg = "Just a String"

scr = cur.initscr()
rows,cols = scr.getmaxyx()

#print message at center of the screen
scr.addstr(rows//2, (cols-len(msg))//2, msg)

scr.hline(cur.LINES//2,0,'_',cur.COLS)

# prints at the bottom of the screen
scr.addstr(rows-2, 0, "this screen has %d rows and %d columns\n"%(rows,cols))
scr.addstr("Try resizing your window(if possible) and"
           + "then rin this program again")

scr.refresh()
scr.getch()
cur.endwin()