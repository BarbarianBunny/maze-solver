from window import Window
from shapes import Line, Point, Cell, Maze

def main():
    bg_color = "gray30"
    line_color = "gray50"
    win = Window(600, 600, bg_color)
    maze = Maze(50, 50, 10, 10, 50, 50, win, line_color, bg_color)

    win.wait_for_close()



main()
