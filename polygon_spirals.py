from turtle import *
shape('turtle')
speed(0)
def polygon(sides,sidelength = 100):
    for i in range(sides):
        forward(sidelength)
        right(360/sides)
def poly_spiral():
    length = 5
    sides = 10
    for i in range(100):
        polygon(sides, length)
        length += 5
        right(5)
        
poly_spiral()
