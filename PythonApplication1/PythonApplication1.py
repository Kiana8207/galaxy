import turtle
import math
from math import * 

screen = turtle.Screen()
screen.tracer(50)

sun =turtle.Turtle()
sun.shape('circle')
sun.color('yellow')

class planet(turtle.Turtle):
    def __init__(self,name,redius,color):
        super().__init__(shape='circle')
        self.name =name 
        self.redius = redius 
        self.c = color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle = 0
    
    def move(self):
        x = self.redius*cos(self.angle) 
        y = self.redius*sin(self.angle) 

        self.goto(sun.xcor()+x,sun.ycor()+y)

mercury = planet('mercury',40,'grey') 
venus = planet('venus',80,'orange') 
earth = planet('earth',100,'blue') 
mars = planet('mars',150,'red') 
jupiter = planet('jupiter',180,'brown') 
saturn = planet('saturn',230,'pink') 
uranus = planet('uranus',250,'light blue') 
neptune = planet('neptune',280,'black') 

mylist=[mercury,venus,earth,mars,jupiter,saturn,uranus,neptune] 

while True :
    screen.update() 
    for i in mylist :
        i.move()  

    mercury.angle += 0.05 
    venus.angle += 0.03
    earth.angle += 0.1 
    mars.angle += 0.007
    jupiter.angle += 0.02
    saturn.angle += 0.018 
    uranus.angle += 0.016 
    neptune.angle += 0.005 



