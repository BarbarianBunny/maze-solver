from window import Window
from shapes import Line, Point, Cell

def main():
    win = Window(800, 600)
    line = Line(Point(200,200), Point(600,400))
    win.draw_line(line, "black")
    cell_1 = Cell(win, Point(200,200), Point(250,250))
    cell_1.draw()
    cell_2 = Cell(win, Point(250,200), Point(300,250))
    cell_2.draw()
    cell_1.draw_move(cell_2)
    cell_2.draw_move(cell_1, True)

    win.wait_for_close()



main()
