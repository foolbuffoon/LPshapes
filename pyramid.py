class Pyramid:
    #variables
    l = 0.0
    w = 0.0
    s = 0.0

    #constuctor
    def __init__(self):
        self.l = 0.0
        self.w = 0.0
        self.s = 0.0

    def calcVol(self):
        vol = (self.l * self.s * self.w)*(1/3)
        return vol

    def calcSA(self):
        sa = 2*((self.l*self.w)*self.s)+pow((self.l*self.w), 2)
        return sa
