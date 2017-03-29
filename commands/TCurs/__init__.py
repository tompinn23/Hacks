import struct; bits = 8 * struct.calcsize("P")
import sys
vermaj = sys.version_info.major
vermin = sys.version_info.minor
version = (vermaj, vermin)
import os

if os.name == 'nt':
    if bits == 64:
        if version == (3,4):
            sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "\amd64\_34") 
            print("34")
        elif version == (3,5):
            sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "\amd64\_35")
        elif version == (3,6):
            sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "\amd64\_36")
    elif bits == 32:
        if version == (3,4):
            sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "\win32\_34") 
        elif version == (3,5):
            sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "\win32\_35")
        elif version == (3,6):
            sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "\win32\_36")
elif os.name == 'posix':
    import curses as Curses
elif os.name == 'mac':
    import curses as Curses
