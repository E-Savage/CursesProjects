import curses as cur

try:
    # call and return a Window object to the scr variable
    scr = cur.initscr() # i1nitiates curses mode by creating a screen object for us to add all of the stuff to the screen on

    scr.addstr("Hello world") # print on virtual screen
    scr.refresh() # print it on real screen
    
    # getch() automatically does a refresh of the screen but it is better to 
    # call the refresh function to make sure that all the screens are up to date
    scr.getch() # gets user input
finally:
    cur.endwin()