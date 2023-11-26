import curses as cur 

def attr_get(win):
    y,x = win.getmaxyx()
    cy,cx = win.getyx() # stores the current position of the cursor
    last = win.inch(y-1, x-1) # store the last character on teh window
    win.insch(y-1,x-1,' ') # writes a space at bottom right 
    ch = win.inch(y-1, 0) # reads back the character stored there 
    win.insch(y-1, x-1, last) # restores the lost character
    win.move(cy,cx) # restores the cursor to the proper position

    return ch

def main(scr):
    scr.attrset(cur.A_UNDERLINE)
    scr.addstr(0, 0,
               "a big string which I didn't want to fully type")
    scr.refresh()
    cur.napms(1000) 

    # store existing attributes 
    atts = attr_get(scr)
    _,len = scr.getyx() # get teh x position of string

    # now call chgat to change to bold
    scr.chgat(0,0,cur.A_BOLD)
    scr.refresh()
    cur.napms(1000)

    # restore the original attributes 
    scr.chgat(0,0,len,atts)
    scr.refresh()
    cur.napms(1000)

    scr.getch()

cur.wrapper(main)

