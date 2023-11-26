import curses as cur

def main(scr):
    cur.echo()
    scr.clear()
    scr.addstr("Hello, what's your name? ")

    name = scr.getstr().decode('utf8')
    scr.addstr("Nice to meet you ")
    scr.addstr(name, cur.A_BOLD) # I think you can guess what this does

    scr.addstr("\n\nHit enter to exit")
    scr.getch()

cur.wrapper(main)