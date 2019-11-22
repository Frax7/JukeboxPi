import os
import curses
from interface.menu import Menu

class Main(object):
    def __init__(self, screen):
        screen = curses.initscr()
        curses.curs_set(False)

        # maxX and maxY of the screen
        maxY, maxX = screen.getmaxyx()
        songs = Menu(os.listdir("../songs/"), screen, maxY-2, maxX//2, 1, 1)
        songs.display()

curses.wrapper(Main)
    

    
