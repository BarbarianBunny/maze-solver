from window import Window
from shapes import Line, Point, Cell

def main():
    win = Window(800, 600)
    line = Line(Point(200,200), Point(600,400))
    win.draw_line(line, "black")
    cell = Cell(win, Point(200,200), Point(600,400))
    cell.draw()

    win.wait_for_close()



main()
