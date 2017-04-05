
import os
from curses import wrapper
import curses
import time
from . import Global

#This is used for importing curses which happens to be version specific.
class ConnectCommand():
	cur = 0
	ips = []
	def __init__(self):
		self.cur = 0
	
	def Run(self):
		self.ips = list(Global.MyIps.keys())
		d = curses.wrapper(self.main)
		os.system("cls")
		for i, k in enumerate(Global.Computers):
			if k.ip == d:
				self.connect(k, Global.myIp)
				return
	
	def connect(self, k, srcIp):
		print('Connecting: ')
		s = '-'
		for i in range(10):
			time.sleep(0.2)
			print('\r' + s, end='')
			s += '-'
		k.onConnect(srcIp)
	
	def main(self, stdscr):
		curses.curs_set(0)
		stdscr.clear()
		while True:
			self.draw(stdscr)
			c = stdscr.getch()
			if len(self.ips) == 0:
				if c == curses.KEY_ENTER or c == 10 or c == 13:
					break
			if c == curses.KEY_DOWN:
				if not self.cur + 1 > len(self.ips) - 1: self.cur += 1
			elif c == curses.KEY_UP:
				if not self.cur - 1 < 0: self.cur -= 1
			elif c == curses.KEY_ENTER or c == 10 or c == 13:
				stdscr.clear()
				return self.ips[self.cur]
			elif c == 27:
				break
			
		
	def draw(self, stdscr):
		stdscr.border()
		stdscr.addstr(1,1, "Choose the IP you wish to connect to.")
		stdscr.addstr(2,1, "If you have a bounce path saved that will be used as well.")
		if len(self.ips) != 0:
			for i, k in enumerate(Global.MyIps):
				stdscr.addstr(3 + i, 1, k)
			stdscr.addstr(3 + self.cur, 1, self.ips[self.cur] + ": " + Global.MyIps[self.ips[self.cur]], curses.A_REVERSE)
		stdscr.addstr(4, 1, "You have no ip addresses saved.")
		stdscr.addstr(5, 1, "Press enter or esc to exit.")

if __name__ == "__main__":
	c = ConnectCommand()
	c.Run()

