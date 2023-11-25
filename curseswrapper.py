import curses as cur

def main(scr):
    scr.addstr("Hello World")
    scr.refresh()
    scr.getch()

cur.wrapper(main) 