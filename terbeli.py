import math
class kup:
    r,m = 0,0
    def __init__(self,r=1,m=1):
        self.r=r
        self.m=m

    def terfogat(self):
        return 1/3*math.pi*self.r**2*self.m
    
    def felszin(self):
        return math.pi*self.r*self.r+math.pi*self.r*(self.r**2+self.m**2)**(1/2)

#rombusz oldal, szog T=a^2*sin(szog), K=4*a
class rombusz:
    a,alfa = 0,0
    def __init__(self,oldal,szog) -> None:
        self.a = oldal
        self.alfa = szog
    
    def kerulet(self):
        return 4*self.a

    def terulet(self):
        return self.a**2*math.sin(self.alfa)

    def eljaras(self):
        pass