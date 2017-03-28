#Template for command this is the absolute basics.
from curses import wrapper
import locale
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
#This is used for importing curses which happens to be version specific.
#from .TCurs import Curses.wrapper as wrapper
def Run():
    wrapper(main)

def main(stdscr):
    stdscr.clear()
    draw(stdscr)
    stdscr.getch()
def draw(stdscr):
    for i in range(80):
        stdscr.addstr(0, i, str('█'))

if __name__ == "__main__":
    Run()
#Run method is needed as it is called by the prompt,
#this is the start of whatever a command,
#wishes to do.
