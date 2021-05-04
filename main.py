import turtle

def square(origin, size):
  if size % 2 != 0:
      size = size - 1
  calc = size / 2
  turtle.up()
  turtle.goto(origin[0] + calc, origin[1] + calc)
  turtle.down()
  turtle.begin_fill()
  turtle.goto(turtle.xcor(), turtle.ycor() - size)
  turtle.goto(turtle.xcor() - size, turtle.ycor())
  turtle.goto(turtle.xcor(), turtle.ycor() + size)
  turtle.goto(turtle.xcor() + size, turtle.ycor())
  turtle.end_fill()

def triange(origin, size):
  calc = size / 2
  turtle.up()
  turtle.goto(origin[0], origin[1] + calc)
  turtle.down()
  

def meger_sponge(origin, size, count, first=True):
  if first:
    turtle.fillcolor('yellow')
    square(origin, size)
  if count == 0:
    return None
  turtle.fillcolor('black')
  turtle.fillcolor('black')
  calc = size/3
  square(origin, size/3)
  meger_sponge([origin[0]-calc,origin[1]+calc],size/3,count-1,False)
  meger_sponge([origin[0],origin[1]+calc],size/3,count-1,False)
  meger_sponge([origin[0]+calc,origin[1]+calc],size/3,count-1,False)
  meger_sponge([origin[0]+calc,origin[1]],size/3,count-1,False)
  meger_sponge([origin[0]+calc,origin[1]-calc],size/3,count-1,False)
  meger_sponge([origin[0],origin[1]-calc],size/3,count-1,False)
  meger_sponge([origin[0]-calc,origin[1]-calc],size/3,count-1,False)
  meger_sponge([origin[0]-calc,origin[1]],size/3,count-1,False)

def s_triangle(origin, size, count, first=True):
  if first:
    turtle.fillcolor('yellow')
    triange(origin, size)
  if count == 0:
    return None
  triange([origin[0],origin[1]- size/3], size/4)


origin = [0,0]
size = 900
count = 5

turtle.bgcolor("black")
turtle.speed(100)
turtle.hideturtle()
turtle.color('yellow')
meger_sponge(origin, size, 5)
turtle.color('Orange')
turtle.up()
turtle.goto([0,-7])
turtle.write("CS",move=False, align='center', font=("Arial", 100, "bold"))

