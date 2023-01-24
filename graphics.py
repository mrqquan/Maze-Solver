from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.resizable(False,False)
        self.__canvas = Canvas(self.__root,bg="black",height=height,width=width)
        self.__canvas.pack(fill=BOTH,expand=1)
        self.__isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks() 
        self.__root.update()

    def wait_for_close(self):
        self.__isRunning = True
        while self.__isRunning:
            self.redraw()
        print("Window Closed")
    
    def draw_line(self, line, fill_color="white"):
        line.draw(self.__canvas,fill_color)

    def close(self):
        self.__isRunning = False

class Point():
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

class Line():
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x,self.p1.y,self.p2.x,self.p2.y,fill = fill_color, width = 2)
        canvas.pack(fill = BOTH, expand = 1)

class Cell():
    def __init__(self,win):
        self.has_left_wall  = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None 
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
    
    def draw(self,x1,y1,x2,y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        fill_color = "black"
        left_line = Line(Point(self._x1,self._y1),Point(self._x1,self._y2))
        if self.has_left_wall:
            self._win.draw_line(left_line)
        else:
            self._win.draw_line(left_line,fill_color)

        right_line = Line(Point(self._x2,self._y1),Point(self._x2,self._y2))
        if self.has_right_wall:
            self._win.draw_line(right_line)
        else:
            self._win.draw_line(right_line,fill_color)
        
        top_line = Line(Point(self._x1,self._y1),Point(self._x2,self._y1))
        if self.has_top_wall:
            self._win.draw_line(top_line)
        else:
            self._win.draw_line(top_line,fill_color)

        bottom_line = Line(Point(self._x1,self._y2),Point(self._x2,self._y2))
        if self.has_bottom_wall:
            self._win.draw_line(bottom_line)
        else:
            self._win.draw_line(bottom_line,fill_color)
    
    def get_center(self):
        return Point((self._x1 + self._x2) / 2,(self._y1 + self._y2) / 2)

    def draw_move(self,to_cell, undo=False):
        fill_color = "green"
        if undo:
            fill_color = "red"

        self._win.draw_line(Line(self.get_center(), to_cell.get_center()),fill_color)


        

