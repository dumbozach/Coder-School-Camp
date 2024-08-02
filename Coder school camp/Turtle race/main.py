from turtle import *
from turtle import Screen
import random
screen = Screen()
screen.colormode(255)

speed(0)
penup()
goto(-140,140)

for label in range(16):
  write(label, align="center")
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)

zach = Turtle()
zach.color("blue")
zach.shape("turtle")
zach.penup()
zach.goto(-160,100)
zach.pendown()

jay = Turtle()
jay.color("red")
jay.shape("turtle")
jay.penup()
jay.goto(-160,50)
jay.pendown()

t3 = Turtle()
t3.color("yellow")
t3.shape("turtle")
t3.penup()
t3.goto(-160,0)
t3.pendown()

zach.speed(random.randint(1,10))
jay.speed(random.randint(1,10))
t3.speed(random.randint(1,10))

while zach.xcor() < 160 and jay.xcor() < 160 and t3.xcor() <160:
  zach.fd(random.randint(1,10))
  jay.fd(random.randint(1,10))
  t3.fd(random.randint(1,10))
  zach.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
  jay.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
  t3.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))


if zach.xcor() >= 160:
  print("Zach is the winner!")
  
if jay.xcor() >= 160:
  print("Jay is the winner!")

if t3.xcor() >= 160:
  print("Turtle 3 is the winner!")