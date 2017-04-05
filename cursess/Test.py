#!/usr/bin/env python
# encoding: utf-8
import npyscreen
import curses
#npyscreen.disableColor()
import sys
sys.path.append('../')
from game.ComputerGenerator import ComputerGenerator

	
class MultiLineActionBoxed(npyscreen.BoxTitle):
	_contained_widgets = npyscreen.MultiLineAction

class DirectoryForm(npyscreen.Form):
	value_list = []
	def create(self):
		c = ComputerGenerator()
		v_list = c.GenerateIPS(200)
		c_list = c.GenerateCompanies(400)
		c_list = list(set(c_list))
		for i in range(200):
			self.value_list.append(v_list[i] +": "+c_list[i])
		self.searchLabel = self.add(npyscreen.FixedText, value='Search:')
		self.searchText = self.add(npyscreen.Textfield)
		self.searchText.add_handlers({curses.ascii.CR: self.h_search_enter, curses.ascii.NL: self.h_search_enter})
		self.directory = self.add(MultiLineActionBoxed,
						max_height=20,
						name='Computers',
						values=self.value_list, 
						slow_scroll=False)
	
	def afterEditing(self):
		self.parentApp.setNextForm(None)
		
	def h_search_enter(self, input):
		self.directory.values = [ val for val in self.value_list if self.searchText.value.upper() in val.upper() ]
		self.directory.display()
class MyApplication(npyscreen.NPSAppManaged):
	def onStart(self):
		self.addForm('MAIN', DirectoryForm, name='Computer Directory')

if __name__ == '__main__':
	TestApp = MyApplication().run()