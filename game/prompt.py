from cmd import Cmd
import shutil
import os
class MyPrompt(Cmd):

	def do_hello(self, args):
		"""Says hello. If you provide a name, it will greet you with it."""
		pass

	def postcmd(self, stop, line):
		if line == 'curses':
			os.system("cls")

	def do_quit(self, args):
		"""Quits the program."""
		print("Quitting.")
		raise SystemExit

	def do_disclaimer(self, args):
		"""Displays the disclaimer"""
		columns = shutil.get_terminal_size().columns
		print("This is a work of fiction.".center(columns))
		print("Names, characters, places and incidents either are products".center(columns))
		print("of the author's imagination or are used fictitiously.".center(columns))
		print("Any resemblance to actual events or locales or persons,".center(columns))
		print("living or dead, is entirely coincidental.".center(columns))
		input()
		os.system('cls')
	
	def do_startmessage(self, args):
		"""Displays the starting message"""
		print("Welcome to hacks")
		print("If you have a save file use the load command")
		print("If you have not played this game before the help command")
		print("is the best place to start")
	
	def do_help(self, arg):
		'List available commands with "help" or detailed help with "help cmd".'
		if arg:
			# XXX check arg syntax
			try:
				func = getattr(self, 'help_' + arg)
			except AttributeError:
				try:
					doc = getattr(self, 'do_' + arg).__doc__
					if doc:
						self.stdout.write("%s\n" % str(doc))
						return
				except AttributeError:
					pass
				self.stdout.write("%s\n" % str(self.nohelp % (arg,)))
				return
			func()
		else:
			names = self.get_names()
			noms = list(vars(self).keys())
			for nom in noms:
				if nom[:5] == 'help_':
					names.append(nom)
				if nom[:3] == 'do_':
					names.append(nom)
			cmds_doc = []
			cmds_undoc = []
			help = {}
			for name in names:
				if name[:5] == 'help_':
					help[name[5:]] = 1
			names.sort()
			# There can be duplicates if routines overridden
			prevname = ''
			for name in names:
				if name[:3] == 'do_':
					if name == prevname:
						continue
					prevname = name
					cmd = name[3:]
					if cmd in help:
						cmds_doc.append(cmd)
						del help[cmd]
					elif getattr(self, name).__doc__:
						cmds_doc.append(cmd)
					else:
						cmds_undoc.append(cmd)
			self.stdout.write("%s\n" % str(self.doc_leader))
			self.print_topics(self.doc_header, cmds_doc, 15, 80)
			self.print_topics(self.misc_header, list(help.keys()), 15, 80)
			self.print_topics(self.undoc_header, cmds_undoc, 15, 80)