import curses
from .Computer import Computer
import commands.Global as Global
import npyscreen
import os
from math import *
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)

class NetInformationCenter(Computer):
	def __init__(self, ip, name, isCorporation, isPerson, netInfoVis):
		Computer.__init__(self, ip, name, isCorporation, isPerson, netInfoVis)
		
		
	def onConnect(self, srcIp):
		app = MyApplication().run()
		os.system('cls')

class MultiLineActionBoxed(npyscreen.BoxTitle):
	_contained_widgets = npyscreen.MultiLineAction

class DirectoryForm(npyscreen.Form):
	value_list = []
	def create(self):
		for i, k in enumerate(Global.Computers):
			if k.netInfoVis:
				self.value_list.append(k.ip + ": "+ k.name)
		self.searchLabel = self.add(npyscreen.FixedText, value='Search:')
		self.searchText = self.add(npyscreen.Textfield)
		self.searchText.add_handlers({curses.ascii.CR: self.h_search_enter, curses.ascii.NL: self.h_search_enter, curses.ascii.ESC: self.h_exit, 27: self.h_exit})
		self.directory = self.add(MultiLineActionBoxed,
						max_height=20,
						name='Computers',
						values=self.value_list, 
						slow_scroll=False)
		self.searchLabel.add_handlers({curses.ascii.ESC: self.h_exit, 27: self.h_exit})
		self.directory.add_handlers({curses.ascii.ESC: self.h_exit, 27: self.h_exit})
	
	def afterEditing(self):
		self.parentApp.setNextForm(None)
		
	def h_search_enter(self, input):
		self.directory.values = [ val for val in self.value_list if self.searchText.value.upper() in val.upper() ]
		self.directory.display()
	
	def h_exit(self, input):
		logging.info("Worked")
		self.parentApp.switchForm('MAIN')

class MainForm(npyscreen.Form):
	def create(self):
		self.help = "lol"
		curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_CYAN)
		highlightText = curses.color_pair(1)
		self.title = self.add(npyscreen.FixedText, value='Net Information Center:')
		self.DirButton = self.add(npyscreen.ButtonPress, name='Computer Directory', cursor_color=curses.COLOR_BLACK, color=curses.COLOR_BLACK, when_pressed_function=self.but_directory)
		self.nextrely -= 1
		self.nextrelx += 21
		self.AdminButton = self.add(npyscreen.ButtonPress, name='Admin', cursor_color=curses.COLOR_BLACK, color=curses.COLOR_BLACK)
	
	def but_directory(self):
		self.parentApp.switchForm('DIR')

class MyApplication(npyscreen.NPSAppManaged):
	def onStart(self):
		self.addForm('MAIN', MainForm, name='Network Information Center')
		self.addForm('DIR', DirectoryForm, name='Computer Directory')