
'''
from turtle import *
begin_fill()
color("orange")
for i in range(6) :
    circle(50,220)
    left(200)
end_fill()

exitonclick()
'''
from turtle import *

def flower(i, j) :
  begin_fill()
  color(j)
  for x in range(6):
    circle(i, 220)
    left(200)
  end_fill()
  exitonclick()

flower(50, "orange")
