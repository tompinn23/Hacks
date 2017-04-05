import sys
sys.path.append("./cursess")
import os
import importlib
import json
from types import MethodType
from game.prompt import MyPrompt
from commands import Global
from game.ComputerGenerator import ComputerGenerator
from game.NetInformationCenter import NetInformationCenter
from game.Computer import Computer

def main():
	"""Main Entry point to the program"""
	prompt = MyPrompt()
	with open("Commands.json", encoding='utf-8') as data_file:
		data = json.loads(data_file.read())
	for i in data['Commands']:
		if i["Command"] == "help":
			continue
		addfunct(i['Command'], i['defaultOutput'], i['className'], prompt)
	prompt.onecmd('disclaimer')
	startGame()
	pp = Global.name + '@localhost~#>'
	prompt.prompt = pp
	test()
	prompt.onecmd('startmessage')
	prompt.cmdloop('')			

def startGame():
	"""Checks if the player has entered name already if not asks them to create name."""
	if os.path.isfile('./name.txt'):
		with open('./name.txt', 'r') as name:
			Global.name = name.read()
	else:
		Global.name = input("Enter your name: ")
		with open('./name.txt', 'w') as name:
			name.write(Global.name)
	GenerateIPs()
	
def GenerateIPs():
	"""This generates random ips for companies and people"""
	c = ComputerGenerator()
	IPS = c.GenerateIPS(400)
	IPComps = IPS[:200]
	IPNames = IPS[-200:]
	Companies = c.GenerateCompanies(300)
	Names = c.GenerateNames(250)
	Companies = list(set(Companies))
	Names = list(set(Names))
	CompDict = {}
	NameDict = {}
	for i, k in enumerate(IPComps):
		CompDict[k] = Companies[i]
	for i, k in enumerate(IPNames):
		NameDict[k] = Names[i]
	Global.AllIps = IPS
	IPS.append('10.66.66.66')
	for i, k in enumerate(CompDict):
		c = Computer(k, CompDict[k], True, False, True)
		Global.Computers.append(c)
	for i, k in enumerate(NameDict):
		c = Computer(k, NameDict[k], False, True, False)
		Global.Computers.append(c)
	
	
def create_command_funct(name, help, cmdMod):
	"""Generator function for dynamically adding commands to the prompt system"""
	c = cmdMod()
	def do_cmd(self, args):
		print("You ran " + cmdMod.__name__ + " command")
		c.Run()
	do_cmd.__name__ = "do_" + name
	do_cmd.__doc__ = help
	return do_cmd

def addfunct(name, help, className, prompt):
	"""Wrapper function for generator function that gets the required parts together,
	   e.g. The Command class
	   Also adds the command to the prompt class"""
	try:
		cmdMod = importlib.import_module("commands." + className)
		try:
			cmdClass = getattr(cmdMod, className)
		except AttributeError:
			return
	except ImportError:
		return
	c = create_command_funct(name, help, cmdClass)
	setattr(prompt, c.__name__, MethodType(c, prompt))

def test():
	Global.PastIPS.append('10.66.66.66')
	Global.PastIPS.append('10.23.365.456')
	n = NetInformationCenter('10.66.66.66', 'Net Information Center', True, False, True)
	c = Computer('10.23.365.456', 'Test 1', True, False, True)
	Global.Computers.append(n)
	#for i, k in enumerate(Global.Computers):
	#	print(k.name + ": " + k.ip)

if __name__ == '__main__':
	main()
	
