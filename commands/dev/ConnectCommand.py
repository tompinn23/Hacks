
from curses import wrapper
import curses
import locale
ips = ['1.1.1.1','1.1.1.2','1.1.1.3','1.1.1.4','1.1.1.5']
cur = 0

#This is used for importing curses which happens to be version specific.
#from .TCurs import Curses.wrapper as wrapper
def Run():
    d = wrapper(main)
    print(d)

def main(stdscr):
    global cur
    curses.curs_set(0)
    stdscr.clear()
    while True:
        draw(stdscr)
        c = stdscr.getch()
        if c == curses.KEY_DOWN:
            if not cur + 1 > len(ips) - 1: cur += 1
        elif c == curses.KEY_UP:
            if not cur - 1 < 0: cur -= 1
        elif c == curses.KEY_ENTER or c == 10 or c == 13:
            return ips[cur]
        elif c == 27:
            break
        
    
def draw(stdscr):
    stdscr.border()
    stdscr.addstr(1,1, "Choose the IP you wish to connect to.")
    stdscr.addstr(2,1, "If you have a bounce path saved that will be used as well.")
    for i, k in enumerate(ips):
        stdscr.addstr(3 + i, 1, k)
    stdscr.addstr(3 + cur, 1, ips[cur], curses.A_REVERSE)

if __name__ == "__main__":
    Run()
#Run method is needed as it is called by the prompt,
#this is the start of whatever a command,
#wishes to do.
