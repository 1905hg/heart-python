import math
from turtle import *

def heart1(M):
    return 15 * math.sin(M) ** 3

def heart2(M):
    return 12*math.cos(M)-5*\
    math.cos(2*M)-2*\
    math.cos(3*M)-\
    math.cos(4*M)

speed(0)
bgcolor("black")

for i in range(600):
    goto(heart1(i)*25, heart2(i)*25)
    goto(0, 0)
    for j in range(1):
        color("red")

done()