import struct; bits = 8 * struct.calcsize("P")
import sys
vermaj = sys.version_info.major
vermin = sys.version_info.minor
version = (vermaj, vermin)


if bits == 64:
    from amd64 import _34, _35, _36
    if version == (3,4):
        from _34 import curses as Curses
        print("34")
    elif version == (3,5):
        from _35 import curses as Curses
    elif version == (3,6):
        from _36 import curses as Curses
elif bits == 32:
    from win32 import _34, _35, _36
    if version == (3,4):
        from _34 import curses as Curses
    elif version == (3,5):
        from _35 import curses as Curses
    elif version == (3,6):
        from _36 import curses as Curses
        
