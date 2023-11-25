import curses

def draw_title(stdscr):
    # Clear the screen
    stdscr.clear()

    # Get screen size
    height, width = stdscr.getmaxyx()

    # Define the title text
    title_text = "Your Title Here"

    # Calculate the position to center the title
    title_y = height // 2 - 3
    title_x = (width - len(title_text)) // 2

    # Draw the title
    stdscr.addstr(title_y, title_x, title_text, curses.A_BOLD)

    # Define button labels
    button1_label = "Text input here"
    button2_label = "Help Button"

    # Calculate button positions
    button1_y = height // 2
    button1_x = (width - len(button1_label)) // 2 - 10

    button2_y = height // 2
    button2_x = (width - len(button2_label)) // 2 + 5

    # Draw buttons
    draw_button(stdscr, button1_y, button1_x, button1_label, selected=True)
    draw_button(stdscr, button2_y, button2_x, button2_label)

    # Update the screen
    stdscr.refresh()

    # Wait for a key press
    key = stdscr.getch()

def draw_button(stdscr, y, x, label, selected=False):
    # Draw the button box
    button_width = len(label) + 4
    stdscr.addch(y - 1, x - 2, curses.ACS_ULCORNER)
    stdscr.addch(y - 1, x + button_width - 1, curses.ACS_URCORNER)
    stdscr.addch(y + 1, x - 2, curses.ACS_LLCORNER)
    stdscr.addch(y + 1, x + button_width - 1, curses.ACS_LRCORNER)
    stdscr.hline(y - 1, x - 1, curses.ACS_HLINE, button_width - 3)
    stdscr.hline(y + 1, x - 1, curses.ACS_HLINE, button_width - 3)
    stdscr.vline(y, x - 2, curses.ACS_VLINE, 2)

    # Draw the button label
    label_x = x
    label_y = y
    if selected:
        stdscr.addstr(label_y, label_x, f" {label} ", curses.A_REVERSE)
    else:
        stdscr.addstr(label_y, label_x, f" {label} ")

if __name__ == "__main__":
    # Run the curses application
    curses.wrapper(draw_title)
