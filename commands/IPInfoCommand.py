from . import Global

class IPInfoCommand():
	def __init__(self):
		pass
	
	def Run(self):
		for i, k in enumerate(Global.PastIPS, 1):
			print(str(i) + ") " + k)
		
		sel = input()
		c = Global.PastIPS[int(sel) - 1]
		try:
			nom = Global.AllCompanies[c]
		except KeyError:
			try:
				nom = Global.AllNames[c]
			except KeyError:
				pass
		print(c + " is the ip for " + nom) 
		print("Do you wish to add this to your ips")
		p = input()
		if p.upper() == "Y" or p.upper() == "YES":
			if not c in Global.MyIps: Global.MyIps[c] = nom
		
				