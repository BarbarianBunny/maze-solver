import time

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, window, top_left_point, bottom_right_point, line_color, background):
        self._win = window
        self._tl_point = top_left_point
        self._br_point = bottom_right_point
        self._tr_point = Point(self._br_point.x, self._tl_point.y)
        self._bl_point = Point(self._tl_point.x, self._br_point.y)
        self._line_color = line_color
        self._background = background
        self.has_bottom_wall = True
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True

    def draw(self):
        # Bottom wall
        line = Line(self._bl_point, self._br_point)
        color = self._line_color if self.has_bottom_wall else self._background
        line.draw(self._win.canvas, color)
        # Left wall
        line = Line(self._tl_point, self._bl_point)
        color = self._line_color if self.has_left_wall else self._background
        line.draw(self._win.canvas, color)
        # Right wall
        line = Line(self._tr_point, self._br_point)
        color = self._line_color if self.has_right_wall else self._background
        line.draw(self._win.canvas, color)
        # Top wall
        line = Line(self._tl_point, self._tr_point)
        color = self._line_color if self.has_top_wall else self._background
        line.draw(self._win.canvas, color)

    def center(self):
        x = (self._tl_point.x + self._br_point.x) // 2
        y = (self._tl_point.y + self._br_point.y) // 2
        return Point(x, y)
    
    def draw_move(self, to_cell, undo=False):
        line = Line(self.center(), to_cell.center())
        if undo:
            line.draw(self._win.canvas, "white")
        else:
            line.draw(self._win.canvas, "red")


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, line_color, bg_color):
        self.x1 = x1 
        self.y1 = y1 
        self.num_rows = num_rows 
        self.num_cols = num_cols 
        self.cell_size_x = cell_size_x 
        self.cell_size_y = cell_size_y 
        self._win = win 
        self._line_color = line_color
        self._bg_color = bg_color
        self._cells = []
        self._create_cells()
        self._draw_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for col_num in range(self.num_cols):
            self._cells.append([])
            col = self._cells[col_num]
            for row_num in range(self.num_rows):
                tx = self.x1 + col_num * self.cell_size_x
                ty = self.y1 + row_num * self.cell_size_y
                bx = tx + self.cell_size_x
                by = ty + self.cell_size_y
                col.append(Cell(self._win, Point(tx, ty), Point(bx, by), self._line_color, self._bg_color))
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _draw_cells(self):
        for col in self._cells:
            for cell in col:
                cell.draw()

    def _draw_cell(self, col, row):
        self._cells[col][row].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(.5)