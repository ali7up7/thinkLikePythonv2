import turtle
import math

t = turtle.Turtle()
numberOfSides= 60

def routeCirlce(radius):
    numberOfSides = countSide(radius)
    routePolygon(numberOfSides)


def countSide(radius):
    return 2*math.pi*radius / numberOfSides


def routePolygon(side):
    for i in range(numberOfSides):
        forwardAndTurnToRight(side)


def forwardAndTurnToRight(side):
    t.fd(side)
    exteriorAngle = countExteriorAngle(numberOfSides)
    t.rt(exteriorAngle)

def countExteriorAngle(numberOfSides):
    return 360/numberOfSides

def routeZ(ali):
    ali.fd(100)
    ali.rt(135)
    ali.fd(int(100 * math.sqrt(2)))
    ali.lt(135)
    ali.fd(100)


routeCirlce(80)
turtle.mainloop()


