import curses

curses.setupterm()
print(curses.tigetstr('clear').decode('ascii'))