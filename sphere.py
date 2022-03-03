import math
class Sphere:
    #variables
    r = 0.0

    #constuctor
    def __init__(self):
        self.r = 0.0

    def calcVol(self):
        vol = (4/3)*math.pi*(self.r**3)
        return vol

    def calcSA(self):
        sa = 4*math.pi*(self.r**2)
        return sa
