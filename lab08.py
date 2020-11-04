#warmup2
def print_matrix():
    mat = []
    ls = [0,0,0,0]
    for i in range(4):
        mat.append(ls)
        print(ls)
        print(mat)
        mat[i][i] = 5
        print(mat)
    print(mat)

def print_matrix2():
    mat = []
    for i in range(4):
        ls = [0,0,0,0]
        mat.append(ls)
        mat[i][i] = 5
    print(mat)

#stretch
def shortest_dist(nested):
  distance=[]
  for i in nested:
    for j in nested:
      if j != i:
        distance.append(dist(i,j))
        #print(distance)
  shortest=min(distance)
  return shortest

def dist(pt1,pt2):
  x1=pt1[0]
  x2=pt2[0]
  y1=pt1[1]
  y2=pt2[1]
  distance=float(((x2-x1)**2+(y2-y1)**2)**0.5)
  return distance

#workout
import turtle
import random

def turtle_race(num_turtles):
    # Make the window boundaries (0,0) and (100,100)
    turtle.setworldcoordinates(0,0,100,100)
    turtle.delay(0)
    turtle_list = []
    #Draw the finish line
    turtle.setpos(90, -100)
    turtle.setpos(90, 200)
    for i in range(num_turtles):
        tr = turtle.Turtle()
        tr.speed(0)
        tr.shape('turtle')
        r = random.random()
        g = random.random()
        b = random.random()
        tr.color(r,g,b)
        tr.penup()
        #Try to spread turtles out evenly
        y = 10 + 80*i/(num_turtles-1)
        tr.setpos(10, y)
        tr.pendown()
        turtle_list.append(tr)
    #print(turtle_list)

    while done(turtle_list):
      for i in range(len(turtle_list)):
        turtle_list[i].forward(random.randint(1,5))
        if turtle_list[i].xcor() >= 90:
          turtle_list[i].turtlesize(3)

def done(turtle_list):
  for i in turtle_list:
    if i.xcor() < 90:
      return True
    else:
      return False
