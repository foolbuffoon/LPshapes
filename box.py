class Box:
    #variables
    l = 0.0
    w = 0.0
    h = 0.0

    #constuctor
    def __init__(self):
        self.l = 0.0
        self.w = 0.0
        self.h = 0.0

    def calcVol(self):
        vol = self.l * self.h * self.w
        return vol

    def calcSA(self):
        sa = 2*(self.l * self.w) + 2*(self.l * self.h) + 2*(self.h * self.w)
        return sa
