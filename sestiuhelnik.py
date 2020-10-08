from turtle import forward, left, right, shape, exitonclick

shape = 'turtle'

delka = 50
uhel = 60
for y in range(6):
    for i in range(6):
        forward(delka)
        left(uhel)
    forward(delka)
    right(uhel)

exitonclick()