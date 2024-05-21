#!/usr/bin/python3
from turtle import Turtle as t

r1 = t()
r2 = t()
s1 = t()
s2 = t()

# t.getscreen()
# turtle features
r1.shape("turtle")
r1.color("red", "green")

# turtle speed
r1.speed(1)

# shape tracing and dimensions
r1.begin_fill()
r1.fd(100)
r1.lt(90)
r1.fd(100)
r1.lt(90)
r1.fd(100)
r1.lt(90)
r1.fd(100)
r1.end_fill()


r1.screen.mainloop()
