import sys
sys.path.append('../')
import commands.Global
import random
import json

startComp = 22
endComp = 28

class ComputerGenerator():
    maxIP = 0
    def __init__(self, ipsToGen):
        self.maxIP = ipsToGen

    def GenerateIPS(self):
        ips = []
        for i in range(self.maxIP):
            fst = random.randint(0,255)
            snd = random.randint(0,255)
            thd = random.randint(0,255)
            fth = random.randint(0,255)
            ip = str(fst) + '.' + str(snd) + '.' + str(thd) + '.' + str(fth)
            ips.append(ip)
        return ips

    def GenerateCompanies(self, maxComp):
        comps = []
        with open('Names.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        st = data["CompaniesFirst"]
        end = data["CompaniesLast"]
        for i in range(maxComp):
            comp = st[random.randint(0, 21)] + ' ' + end[random.randint(0,27)]
            comps.append(comp)
        return comps

    def GenerateNames(self, maxNames):
        names = []
        with open('Names.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        fs = data["PeopleFirst"]
        sr = data["PeopleLast"]
        for i in range(maxNames):
            comp = fs[random.randint(0, 89)] + ' ' + sr[random.randint(0,79)]
            names.append(comp)
        return names

if __name__ == "__main__":
    c = ComputerGenerator(400)
##    t = c.GenerateIPS()
##    print(len(t))
##    input()
##    tp = list(set(t))
##    print(len(tp))
##    input()
##    for i in t:
##        print(i)
##    k = c.GenerateCompanies(250)
##    print(len(k))
##    input()
##    kp = list(set(k))
##    print(len(kp))
##    input()
##    for j in kp:
##        print(j)
    k = c.GenerateNames(400)
    print(len(k))
    input()
    kp = list(set(k))
    print(len(kp))
    input()
    for j in kp:
        print(j)
    
    
    
