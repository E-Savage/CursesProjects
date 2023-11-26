import curses as cur

prompt = "Enter a string:"

try:
    scr = cur.initscr()
    rows,cols = scr.getmaxyx()

    scr.addstr(rows//2, (cols-len(prompt))//2, prompt)
    bs = scr.getstr() # gets user input from a byte string

    scr.addstr(cur.LINES-2, 0, 
               "You entered: %s"%bs.decode('utf-8'))
    
    scr.getch()
finally:
    cur.endwin()
