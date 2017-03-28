#Template for command this is the absolute basics.

#This is used for importing curses which happens to be version specific.
from .TCurs import Curses.wrapper as wrapper
def Run():
    pass

#Run method is needed as it is called by the prompt,
#this is the start of whatever a command,
#wishes to do.
