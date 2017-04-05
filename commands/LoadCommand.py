from . import Global
import os
class LoadCommand():
	def __init__(self):
		pass
	
	def Run(self, filename):
		with open("../saves/" + filename + ".hck", mode='rb') as save_file:
			save = pickle.loads(save_file.read())
		Global.AllIps = save[0] 
		Global.AllCompanies = save[1]
		Global.AllNames = save[2]
		Global.MyIps = save[3]
	
			
		
