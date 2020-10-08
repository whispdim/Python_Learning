from turtle import shape, forward, penup, pendown, exitonclick

for delka in range(20):
    pendown()
    forward(delka)
    penup()
    forward(10)

exitonclick()