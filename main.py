import turtle

def square(origin, t, size):
    if size % 2 != 0:
        size = size - 1
    calc = size / 2
    t.up()
    t.goto(origin[0] + calc, origin[1] + calc)
    t.down()
    t.goto(t.xcor(), t.ycor() - size)
    t.goto(t.xcor() - size, t.ycor())
    t.goto(t.xcor(), t.ycor() + size)
    t.goto(t.xcor() + size, t.ycor())

def triange(origin, size):
  calc = size / 2
  turtle.up()
  turtle.goto(origin[0], origin[1] + calc)
  turtle.down()
  turtle.right(120)
  turtle.forward(size)
  turtle.left(120)
  turtle.forward(size)
  turtle.left(120)
  turtle.forward(size)
  turtle.setheading(0)

def meger_sponge(origin, size, count, t, first=True):
    if first:
        t.fillcolor('blue')
        square(origin, t, size)
    if count == 0:
        return None
    calc = size/3
    square(origin, size/3,t)
    meger_sponge([origin[0]-calc,origin[1]+calc],size/3,count-1,t,False)
    meger_sponge([origin[0],origin[1]+calc],size/3,count-1,t,False)
    meger_sponge([origin[0]+calc,origin[1]+calc],size/3,count-1,t,False)
    meger_sponge([origin[0]+calc,origin[1]],size/3,count-1,False)
    meger_sponge([origin[0]+calc,origin[1]-calc],size/3,count-1,t,False)
    meger_sponge([origin[0],origin[1]-calc],size/3,count-1,t,False)
    meger_sponge([origin[0]-calc,origin[1]-calc],size/3,count-1,t,False)
    meger_sponge([origin[0]-calc,origin[1]],size/3,count-1,t,False)


turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.color('white')
meger_sponge([0,0], 700, 6, t, first=True)