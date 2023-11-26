import curses as cur

def show_status(win, txt):
    # display text un bottom line of screen 
    ht, wd = win.getmaxyx()
    win.addstr(ht-1, 1, txt)
    win.clrtoeol()
    win.refresh()

def main(scr):
    # create the main window 
    win = cur.newwin(16, 50, 4, 4)
    win.box()
    win.addstr(4, 7, "Main Window")
    show_status(scr, "Created main window")
    win.refresh()
    scr.getch()

    # add sub-window of main 
    sw = win.subwin(4, 18, 6, 9) # use screen coords
    sw.box()
    sw.addstr(1, 2, "Sub-window") # use sub win coords
    sw.refresh()
    show_status(scr, "Sub-window creates a view into main window")
    scr.getch()

    # add derived window of main 
    dw = win.derwin(4, 18, 6, 9)
    dw.box()
    dw.addstr(1, 2, "Derived Window")
    dw.refresh()
    show_status(scr, "Derived window is the same but uses realtive coords")
    scr.getch()

    # add new window on top of main
    nw = cur.newwin(4, 18, 15, 6)
    nw.box()
    nw.addstr(1, 2, "New Window")
    nw.refresh()
    show_status(scr, "new window on top of the main window ")
    scr.getch()

    # move main window, including sub-windows
    scr.touchwin()
    scr.refresh()
    win.mvwin(2, 10)
    win.refresh()
    nw.touchwin()
    nw.refresh()
    show_status(scr, 
                "Move main window with sub-window" +
                "newwin is not affected")
    scr.getch()

    # clear main window - includes subwindow and border
    win.clear()
    win.refresh()
    nw.touchwin()
    nw.refresh()
    show_status(scr,
                "Clear main window text and borders" +
                ", newwin untouched")
    scr.getch()

    #redraw just the borders
    win.box()
    sw.box()
    dw.box()
    win.refresh()
    nw.touchwin()
    nw.refresh()
    show_status(scr, "redrawing borders shows window object still exists")
    scr.getch()

cur.wrapper(main)