import curses as cur

ch = -1
delay = True

try:
    scr = cur.initscr()
    # cur.nocbreak()
    # cur.raw()
    # cur.cbreak()
    # scr.nodelay(True)

    scr.addstr("Type something here:")
    scr.refresh()
    if delay:
        ch = scr.getch()
    else:
        while ch == 1:ch = scr.getch()
    scr.addstr("\nYou typed: %s"%chr(ch))
    scr.refresh()
    cur.napms(1000)
finally:
    cur.endwin()