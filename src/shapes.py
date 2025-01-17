

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
    def __init__(self, window, top_left_point, bottom_right_point):
        self._win = window
        self._tl_point = top_left_point
        self._br_point = bottom_right_point
        self._tr_point = Point(self._br_point.x, self._tl_point.y)
        self._bl_point = Point(self._tl_point.x, self._br_point.y)
        self.has_bottom_wall = True
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True

    def draw(self):        
        if self.has_bottom_wall:
            line = Line(self._bl_point, self._br_point)
            line.draw(self._win.canvas, "black")
        if self.has_left_wall:
            line = Line(self._tl_point, self._bl_point)
            line.draw(self._win.canvas, "black")
        if self.has_right_wall:
            line = Line(self._tr_point, self._br_point)
            line.draw(self._win.canvas, "black")
        if self.has_top_wall:
            line = Line(self._tl_point, self._tr_point)
            line.draw(self._win.canvas, "black")

    def center(self):
        x = (self._tl_point.x + self._br_point.x) // 2
        y = (self._tl_point.y + self._br_point.y) // 2
        return Point(x, y)
    
    def draw_move(self, to_cell, undo=False):
        line = Line(self.center(), to_cell.center())
        if undo:
            line.draw(self._win.canvas, "gray")
        else:
            line.draw(self._win.canvas, "red")


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1 
        self.y1 = y1 
        self.num_rows = num_rows 
        self.num_cols = num_cols 
        self.cell_size_x = cell_size_x 
        self.cell_size_y = cell_size_y 
        self._win = win 
        self._cells = []
        self._create_cells()
        self._draw_cells()


    def _create_cells(self):
        for col_num in range(self.num_cols):
            self._cells.append([])
            col = self._cells[col_num]
            for row_num in range(self.num_rows):
                tx = self.x1 + col_num * self.cell_size_x
                ty = self.y1 + row_num * self.cell_size_y
                bx = tx + self.cell_size_x
                by = ty + self.cell_size_y
                col.append(Cell(self._win, Point(tx, ty), Point(bx, by)))
        
    def _draw_cells(self):
        for col in self._cells:
            for cell in col:
                cell.draw()