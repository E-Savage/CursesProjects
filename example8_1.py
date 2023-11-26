import curses as cur

def main(scr):
    # basic bordless window
    w1 = cur.newwin(1,80)
    w1.addstr("window 1")
    w1.refresh()
    cur.napms(1000)
    scr.getch()


    # window with box border
    w2 = cur.newwin(3, 50, 10, 5)
    w2.box()
    w2.addstr(1, 1, "Text in a bound box")
    w2.refresh()
    cur.napms(2000)
    scr.getch()

    # default arguments creates fulls screen
    w3 = cur.newwin(0, 0)
    w3.box()
    w3.refresh()
    cur.napms(2000)
    scr.getch()

    # new window with custom border
    w4 = cur.newwin(10, 10, 5, 5)
    w4.border('L', 'R', 'T', 'B', '{','}', '[', ']')
    w4.refresh()
    cur.napms(2000)
    scr.getch()

cur.wrapper(main)