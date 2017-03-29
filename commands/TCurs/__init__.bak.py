import struct; bits = 8 * struct.calcsize("P")
import sys
vermaj = sys.version_info.major
vermin = sys.version_info.minor
version = (vermaj, vermin)
import os

if os.name == 'nt':
    if bits == 64:
        if version == (3,4):
            from .amd64._34 import curses as Curses
            print("34")
        elif version == (3,5):
            from .amd64._35 import curses as Curses
        elif version == (3,6):
            from .amd64._36 import _curses as Curses
    elif bits == 32:
        if version == (3,4):
            from .win32._34 import curses as Curses
        elif version == (3,5):
            from .win32._35 import curses as Curses
        elif version == (3,6):
            from .win32._36 import curses as Curses
elif os.name == 'posix':
    import curses as Curses
elif os.name == 'mac':
    import curses as Curses
