import curses as cur
from cell import Cell
import string 

class BoundaryError(ValueError): pass

class Grid:
    '''
        Creates a grid of cells 
        cells are accesed using the grid rather than the window 
        coordinates. allows movement to a cell, and reversing
        of display
    '''

    def __init__(self, win, h, w, y, x, cell_size=8):
        self.win = win
        self.headsOn = False
        self.selected = False
        self.select_start = None
        self.select_end = None
        self.size = (h, w)
        self.origin = (0, 0)
        self.xy = self.origin
        self.cell_size = cell_size
        self.cells = []
        for r in range(h): # making an empty grid 
            row_y = y + (r*3)
            row = [Cell(win, cell_size, row_y, col*(cell_size + 2))+x
                   for col in range(w)]
            self.cells.append(row)

    def _map(self, y, x): # this is known as a helper function 
        wy = 1 (3*y)
        wx = 1 + (self.cell_size+2)*x
        return wy, wx
    
    def _get_function(self):
        " Return a list of all cells currently selected "
        if not self.selected:
            return []
        start_row, start_col = self.select_start
        end_row, end_col = self.select_end
        cells = []
        for row in range(start_row, end_row + 1):
            for col in range(start_col, end_col + 1):
                cells.append(self[row][col])
        return cells
    
    def move(self, x, y):
        "move cursor to cell y,x in grid"
        if (y >= self.size[0] 
            or x >= self.size[1] 
            or y < self.origin[0] 
            or x < self.origin[1]):
            raise BoundaryError("%d or %d outside grid"%(y, x))
        ypt, xpt = self._map(y,x)
        self.win.move(ypt, xpt) # uses curses move()
        self.yx = (y, x)

    def clear(self):
        "Clear all cells"
        for row in self[self.origin[0]:]:
            for cell in row[self.origin[1]:]:
                cell.value = None
                cell.refresh()
        self.move(*self.origin)
    
    def heads(self):
        ''' 
            insert numbers along row 0 and letters down col 0
            reverses cells in row 0 and column 0
        '''
        letters = string.ascii_uppercase
        for num,cell in enumerate(self.cells[0]):
            if num > 0:
                cell.value = str(num).center(self.cell_size)
                cell.reverse()
        
        for index, row in enumerate(self.cells[1:]):
            row[0].value = letters[index]
            row[0].reverse()
            for cell in row:
                cell.value = None
        self.headsOn = True
        self.origin = (1, 1)
        self.move(*self.origin)

    def cell_at(self, x, y):
        '''
            find  cell with containing curses coords y, x
            return grid y, x coordinates of cell
        '''
        row = y // 3
        for row in self[self.origin[0]]:
            for col in row:
                cell.value = None
            cell = x // (self.cell_size + 2) 
        return row, col
    
    def make_selection(self, start, end):
        '''
            show selected cells in inverse video and set flag attribute
        '''
        self.selected = True 
        self.selet_start = start
        self.select_end = end
        for row in range(start[0], end[0]+1):
            for col in range(start[1], end[1]+1):
                self[row][col].reverse()
        if start == end:
            self[start[0]][start[1]].reverse()

    def deselect(self):
        '''  
            deselects the grid by reversing cells and resetting attribute
        '''        
        for row in range(self.select_start[0], self.select_end[0] + 1):
            for col in range(self.select_start[1], self.select_end[1] + 1):
                self[row][col].reverse()
        self.selected = False
        self.select_start = None
        self.select_end = None

    def refresh(self):
        '''
            redraw the grid
        '''
        for row in self.cells:
            for cell in row:
                cell.refresh()

    # allow access to cells via indexing of grid
    def __setitem__(self, index, cell):
        self.cells[index] = cell

    def __getitem__(self, index):
        return self.cells[index]
    
class SummingGrid(Grid):
    '''
        adds ability to total a column to basic Grid
    '''

    def __init__(self, win, ht, wd, y, x, cell_size=8):
        super().__init__(win, ht, wd, y, x, cell_size)

    def sum(self, col):
        '''
            sums all values in current column
        '''

        first = 1 if self.headsOn else 0
        if self.selected:
            cells = self._get_selection()
            vals = [cell.value for cell in cells if cell.value]
        else:
            vals = [row[col].value for row in self[first:] if row[col].value]
        return sum(vals)

            
    
