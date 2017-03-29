from . import TCurs
import os
from curses import wrapper
import curses
from . import Global

#This is used for importing curses which happens to be version specific.
class ConnectCommand():
    cur = 0
    ips = []
    def __init__(self):
        self.cur = 0
        self.ips = Global.ips
    def Run(self):
        d = curses.wrapper(self.main)
        os.system("cls")
        print(d)

    def main(self, stdscr):
        curses.curs_set(0)
        stdscr.clear()
        while True:
            self.draw(stdscr)
            c = stdscr.getch()
            if c == curses.KEY_DOWN:
                if not self.cur + 1 > len(self.ips) - 1: self.cur += 1
            elif c == curses.KEY_UP:
                if not self.cur - 1 < 0: self.cur -= 1
            elif c == curses.KEY_ENTER or c == 10 or c == 13:
                return self.ips[self.cur]
            elif c == 27:
                break
            
        
    def draw(self, stdscr):
        stdscr.border()
        stdscr.addstr(1,1, "Choose the IP you wish to connect to.")
        stdscr.addstr(2,1, "If you have a bounce path saved that will be used as well.")
        for i, k in enumerate(self.ips):
            stdscr.addstr(3 + i, 1, k)
        stdscr.addstr(3 + self.cur, 1, self.ips[self.cur], curses.A_REVERSE)

if __name__ == "__main__":
    ConnectCommand.Run()

