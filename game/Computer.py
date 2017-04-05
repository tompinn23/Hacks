class Computer():
	ip = ''
	name = ''
	isCorporation = False
	isPerson = False
	netInfoVis = False
	def __init__(self, ip, name, isCorporation, isPerson, netInfoVis):
		self.ip = ip
		self.name = name
		self.isCorporation = isCorporation
		self.isPerson = isPerson
		self.netInfoVis = netInfoVis
