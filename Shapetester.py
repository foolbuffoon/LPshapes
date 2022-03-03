#overhead
import math
from box import Box
from sphere import Sphere
from pyramid import Pyramid
b1 = Box()
s1 = Sphere()
p1 = Pyramid()
#letting the user choose a shape
shapeChoice = int(input('To calculate a cube, press 1, to calculate a sphere, press 2, to calculate a pryramid, press 3 '))
if shapeChoice == 1:
    b1.l = float(input('Length of cube: '))
    b1.w = float(input('Width of cube: '))
    b1.h = float(input('Height of cube: '))
    print("Volume of shape: ", round(b1.calcVol()))
    print("Total surface area of shape: ",  round(b1.calcSA()))
elif shapeChoice == 2:
    s1.r = float(input('Radius of Circle: '))
    print("Volume of shape: ",  round(s1.calcVol()))
    print("Total surface area of shape: ",  round(s1.calcSA()))
elif shapeChoice == 3:
    p1.l = float(input('Length of the Pyramid Base '))
    p1.w = float(input('Width of the Pyramid Base '))
    p1.s = float(input('Pyramid side legth '))
    print("Volume of shape: ",  round(p1.calcVol()),2)
    print("Total surface area of shape: ",  round(p1.calcSA(),))
else:
    print('Please choose an included shape')
