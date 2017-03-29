import random

class ComputerGenerator():
    maxIP = 0
    def __init__(self, ipsToGen):
        self.maxIP = ipsToGen

    def GenerateIPS(self):
        for i in range(self.maxIP):
            fst = random.randint(0,255)
            snd = random.randint(0,255)
            thd = random.randint(0,255)
            fth = random.randint(0,255)
            ip = str(fst) + '.' + str(snd)
