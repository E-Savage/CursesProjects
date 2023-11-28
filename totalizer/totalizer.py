import curses as cur
from grid import Grid, BoundaryError, SummingGrid

# define mouse event indices
X_COORD = 1
Y_COORD = 2
BUTTON_STATE = 4

class Totalizer:
    '''
        Spreadsheet-like grid that can display totals of columns.
        values must be integers
    '''

    help_string = "Press F1 (or H) for help, X to exit"

    def __init__(self, win, ht, wd, cell_size=8):
        self.win = win
        self.size = (ht, wd)
        self.cell_size = cell_size
        self.selecting = False
        self.selection = None
        self.grid = SummingGrid(win, ht, wd, 0, 0, cell_size)
        self.grid.heads()
        cur.mousemask(cur.ALL_MOUSE_EVENTS)

    def _show_status(self, msg):
        '''
            display message on bottom line of the window
        '''

        X,Y = self.win.getmaxyx()
        y,x = self.grid.xy

        # clear line but not border
        self.win.addstr(Y - 2, 1, ''*(X - 2))
        self.win.addstr(Y - 2, 1, msg)
        self.grid.move(y, x)

    def _show_help(self):
        '''
            show help screen in new window, remove window on any key
        '''

        ht, wd = self.win.getmaxyx()
        top = (ht - 15) // 2
        left = (wd - 50) // 2
        win = cur.newwin(15, 5, top, left)
        win.keypad(True) # accepts mouse clicks and special keys
        win.box()

        win.addstr(1, 2, "Accept keys move cursor")
        win.addstr(3, 2, "Mouse positions cursor")
        win.addstr(5, 2, "=N<RETURN> inserts value")
        win.addstr(7, 2, "+Sums the current column")
        win.addstr(9, 2, "S Start/end/cancel/ selection")
        win.addstr(11, 2, "C Clear grid")
        win.addstr(13, 2, "X eXit the application")
        win.refresh()
        win.getch()
        win.erase()
        self.grid.refresh()
        # restore cursor to previous cell
        self.grid.move(*self.gridyx)

        def run(self):
            '''
                start cursor to previous cell
            '''
            Y, X = self.win.getmaxyx()
            self.win.addstr(Y - 3, 1, self.help_string)
            self.grid.move(*self.grid.origin) # starting position

            while True:
                key = self.win.getch()
                if key in [ord('X'), ord('x')]:break
                if key in [cur.KEY_F1, ord('H'), ord('h')]:
                    self._show_help()
                elif key in [cur.KEY_UP, ord('k')]:
                    y, x = self.grid.yx
                    try: self.grid.move(y-1, x)
                    except BoundaryError as e:
                        self._show_statis(e.args[0])
                elif
