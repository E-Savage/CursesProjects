import curses as cur

def main(scr):

    # window with box border and text inside 
    win = cur.newwin(15, 50, 10, 5)
    win.box()
    win.addstr(1, 1, "Text in a bound box")
    win.refresh()
    cur.napms(2000)

    # resize and add string 
    win.resize(5, 30)
    win.addstr(2, 1, "Resized smaller")
    win.box()
    scr.refresh()
    win.refresh()
    cur.napms(2000)

    # move to new position 
    win.mvwin(20, 12)
    win.move(2, 1)
    win.clrtoeol() # remove old text
    win.addstr(2, 1, "Moved box") # insert new text
    win.box()
    scr.touchwin()
    scr.refresh()
    win.refresh()
    cur.napms(2000)

    # scroll window up 1 line
    win.scrollok(True)
    win.scroll(1)
    win.move(3, 1)
    win.clrtoeol()
    win.box()
    win.refresh()
    cur.napms(2000)

    # scroll window down 1 line
    win.scroll(-1)
    win.move(1, 1)
    win.clrtoeol()
    win.box()
    cur.napms(2000)


cur.wrapper(main)
