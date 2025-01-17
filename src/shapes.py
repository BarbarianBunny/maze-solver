

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
