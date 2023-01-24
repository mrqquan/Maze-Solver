from graphics import Window, Point, Line, Cell
from maze import Maze

def main():
    win = Window(800,600)
    m = Maze(50,50,30,30,20,15,win)
    m.solve()
    win.wait_for_close()

main()

