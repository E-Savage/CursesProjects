import curses

def main(win):
    help(win.__class__)

curses.wrapper(main)