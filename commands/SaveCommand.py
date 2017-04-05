from . import Global
import os
class SaveCommand():
	def __init__(self):
		pass
	
	def Run(self, filename):
                save_data = [Global.AllIps, Global.AllCompanies, Global.AllNames, Global.MyIps]
		with open("../saves/" + filename + ".hck", mode='wb') as save_file:
                        save = pickles.dumps(save_data)
                        save_file.write(bytes(save))
		
	
			
		
