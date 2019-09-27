import turtle
from thinkLikePythonv2.polygon import routeArc, t

radius = 100
angle =70


def routeFlower(petals):
    for petal in range(petals):
        routePetal()
        t.rt(int(360/(petals-1)))

def routePetal():
    for i in range(2):
        routeArc(radius, angle)
        t.rt(180-angle)


routeFlower(7)
t.hideturtle()
turtle.mainloop()
