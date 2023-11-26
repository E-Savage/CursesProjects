import curses as cur

class Cell:
    
    def __init__(self, win, w, y, x, val=None):
        self.att = cur.A_NORMAL
        self.width = w
        self.isReversed = False
        self.theCell = win.subwin(3, w+2, y, x)
        self.theCell.box()
        self.value = val 
        self.refresh()

    @property 
    def value(self): return self._value

    @value.setter
    def value(self, v):
        v = v if v else ""
        if len(str(v)) > self.width:
            raise ValueError("%d too large a value for a cell"%v)
        
        self._value = v # actually store the value 
        self.theCell.addstr(1, 1, str(v).ljust(self.width))
        self.refresh()

    def reverse(self):
        self.att = cur.A_NORMAL if self.isReversed else cur.A_REVERSE 
        self.isReversed = not self.isReversed
        self.refresh()

    def refresh(self):
        self.theCell.attrset(self.att)
        self.theCell.box()
        self.theCell.addstr(1, 1, str(self.value).ljust(self.width))

    def __str__(self):
        return str(self.value)
    
