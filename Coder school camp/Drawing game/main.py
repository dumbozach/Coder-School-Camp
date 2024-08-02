import turtle
screen = turtle.Screen()

user = turtle.Turtle()
user.shape("turtle")
user.penup()
user.goto(0, 0)
user.speed(10)

drawing = False

print("Press Z to make a square, X to make a triangle, C to make a circle, V to make a star, E to start free drawing, and SPACE to erase your drawing")

def erase():
   user.clear()

def draw():
  global drawing
  if drawing == False:
    user.shape("classic")
    user.pendown()
    drawing = True
  else:
    user.shape("turtle")
    user.penup()
    drawing = False

if drawing:
    user.pendown()
else:
    user.penup()

def go_to(x, y):
    user.setheading(user.towards(x,y))
    user.goto(x, y)

def square():
    user.pendown()
    for _ in range(4):
        user.forward(100)
        user.right(90)
    user.penup()

def triangle():
    user.pendown()
    for _ in range(3):
        user.forward(100)
        user.left(120)
    user.penup()

def circle():
   user.pendown()
   user.circle(50)
   user.penup()

def star():
   user.pendown()
   for i in range(5):
      user.forward(100)
      user.right(144)
   user.penup()

screen.onclick(go_to)
screen.onkey(draw, "e")
screen.onkey(square, "z")
screen.onkey(triangle, "x")
screen.onkey(circle, "c")
screen.onkey(star, "v")
screen.onkey(erase, "space")
screen.listen()
turtle.mainloop()