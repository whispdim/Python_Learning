from turtle import shape, left, right, exitonclick, forward

shape = 'turtle'

delka = 50
otocka = 90

for x in range(5):
    for y in range(5):
        forward(delka)
        left(otocka)
        forward(delka)
        right(otocka)