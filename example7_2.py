import curses as cur

def main(scr):
    scr.clear()
    scr.addstr("Hello, this is a test string...")
    scr.addstr("\nand this is another" 
               + " underlined", cur.A_UNDERLINE)
    scr.getch()

    scr.move(0,0) # reposition the cursor
    scr.chgat(5 , cur.A_BOLD) # changes the attribute of the first five characters
    scr.getch()

    scr.addstr("oops! ") # overwrites the first few characters on the line 
    scr.getch()
    scr.chgat(0, 5, -1, cur.A_REVERSE) # reverses to EOL from 0 to 5
    scr.getch()

cur.wrapper(main)

