from tkinter import Tk, BOTH, Canvas
from shapes import Line

class Window:
    def __init__(self, width, height, bg_color):
        self.__root = Tk()
        self.__root.title = "window"
        self.canvas = Canvas(self.__root, width=width, height=height, background=bg_color)
        self.canvas.pack()
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
