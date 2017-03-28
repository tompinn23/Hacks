import TCurs

print(TCurs.__dict__)

from TCurs import Curses
def Run():
    stdscr = curses.initscr()
    stdscr.getch()
    curses.endwin()
