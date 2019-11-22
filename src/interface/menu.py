import curses
from curses import panel

class Menu(object):

    def __init__(self, items, stdscreen, nlines, ncols, begin_y, begin_x):
        self.window = stdscreen.derwin(nlines, ncols, begin_y, begin_x)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 0
        self.items = items

    def navigate(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= len(self.items):
            self.position = len(self.items)-1

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.border(0,0,0,0,0,0,0,0)
        self.window.refresh()

        while True:
            self.window.refresh()
            curses.doupdate()
            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL
                msg = '%s' % (item)
                self.window.addstr(1+index, 1, msg, mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                print()

            elif key == curses.KEY_UP:
                self.navigate(-1)

            elif key == curses.KEY_DOWN:
                self.navigate(1)

            elif key == ord('q'):
                break
            
        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()
