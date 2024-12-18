from turtle import *
import time
from random import *

colors = ['red',
'orange',
'yellow',
'green',
'cyan',
'blue',
'indigo',
'violet',
'purple',
'magenta',
'pink',
'brown',
'white',
'gray',
'red',
'orange',
'yellow']
while True:
    goto(300,100)
    speed(0)
    color(choice(colors))
    bgcolor('black')
    b = 200

    while b > 0:
        left(b)
        forward(b*3)
        b = b-1
    time.sleep(1)
    reset()
