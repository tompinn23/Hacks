import shutil
from colorama import init, Fore, Back
init(autoreset=True)
import msvcrt
import kbhit
import math
values = ["Tom","Jack","Alfie","Joss","Kai","Nihal","Ben","Oliver","Josh","Dan","Lindzi","Anna","Amanda","Jess","Freddie","Alex","Harvey","Billy","Anas",	"Martina","Caroline","Faye","Erik","David","Mark","James","Nancy","Pete","Jeremy","Sammy","Ross","Harry","Louis","Ryan","Shaila","Rachel","Dave","Kevin","Bob","Benjamin","Ellen","Connor","Kyle","Charlie","Jacob","Niamh","Rhianna","Esme","Emily","Eleanor","Lewis","Sofia","Gaby","Lola","Haider","Carter","Olivia","Annie","Alicia","Adam","George","Charlotte", "Priya"]

llcorner = '└'
lrcorner = '┘'
tlcorner = '┌'
trcorner = '┐'
cross = '┼'
hline = '─'
vline = '│'
leftT = '├'
rightT = '┤'
bottomT = '┴'
topT = '┬'

kb = kbhit.KBHit()

rowsInBox = 20
startingIndex = 0
current = 0
absIndex = 0
page = 0
pages = math.ceil(len(values)/rowsInBox) - 1
wholeRefresh = True
def clscr():
	print("\33[2J") 

def box(row, col, width, height):
	maxWidth = col + width
	maxHeight = row + height
	for j in range(row, row + height):
		for i in range(col, col + width):
			if i == col and j == row: print('\33[{};{}H'.format(j,i) + tlcorner)
			elif j == row and i == maxWidth - 1: print('\33[{};{}H'.format(j,i) + trcorner)
			elif i == col and j == maxHeight - 1 : print('\33[{};{}H'.format(j,i) + llcorner)
			elif i == maxWidth - 1 and j == maxHeight - 1 : print('\33[{};{}H'.format(j,i) + lrcorner)
			elif i == col or i == maxWidth - 1: print('\33[{};{}H'.format(j,i) + vline)
			elif (j == row or j == maxHeight - 1) and not (i == col or i == maxWidth - 1):  print('\33[{};{}H'.format(j,i) + hline)
			else: print('\33[{};{}H'.format(j,i) + ' ')

			
def putCursor(row=None, col=None):
	if row == None and col == None:
		size = shutil.get_terminal_size((80,20))
		nnPrint('\33[{};0H'.format(size.lines))
	else:
		nnPrint('\33[{};{}H'.format(row,col))

def printAt(row, col, string):
	print('\33[{};{}H{}'.format(row, col, string))
	
def printValues():
	global current
	global wholeRefresh
	if wholeRefresh:
		wholeRefresh = False
		nnPrint('\33[3;3H')
		offset = 0
		for i in range(page * 20, page * 20 + rowsInBox):
			nnPrint('\33[{};{}H'.format(3 + offset,3)+ '                                                  ')
			try:
				nnPrint('\33[{};{}H'.format(3 + offset,3)+ values[i])
			except IndexError:
				pass
			offset += 1
	try:
		print('\33[{};{}H'.format(3+ current, 3) + Fore.BLACK + Back.WHITE + values[current + page * 20])
	except IndexError:
		current = len(values) - page * 20 - 1
		print('\33[{};{}H'.format(3+ current, 3) + Fore.BLACK + Back.WHITE + values[current + page * 20])
	
def getKey():
	global page
	global pages
	global current
	global wholeRefresh
	c = kb.getarrow()
	if c == 0:
		if current > 0:
			current -= 1
			print('\33[{};{}H'.format(3+ current + 1, 3) + Fore.WHITE + Back.BLACK + values[current + page * 20 + 1])
		elif current == 0:
			if page > 0:
				page -= 1
				current = 19
				wholeRefresh = True
			if page == 0:
				
	if c == 1:
		if page < pages:
			page += 1
			wholeRefresh = True
	if c == 2:
		if current < rowsInBox - 1:
			current += 1
			print('\33[{};{}H'.format(3+ current - 1, 3) + Fore.WHITE + Back.BLACK + values[current + page * 20 - 1])
		elif current == 19:
			if page < pages:
				page += 1
				current = 0
				wholeRefresh = True
	if c == 3:
		if not page == 0:
			page -= 1
			wholeRefresh = True
	
	
def nnPrint(string):
	print(string, end="")
kbhit.hide_cursor()
clscr()
box(2,2,52,22)
while True:
	printValues()
	getKey()
input()