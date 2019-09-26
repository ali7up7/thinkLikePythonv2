import turtle
import math

t = turtle.Turtle()
numberOfSides= 60


def routeCirlce(radius):
    routeArc(radius, 360)


def routeArc(radius, angle):
    side = countSide(radius)
    sides = countNumberOfSidesToDraw(angle)
    routePolygon(side, sides)


def degreeToRadian(degree):
    return degree/180*math.pi


def countSide(radius):
    return 2*math.pi*radius / numberOfSides


def countNumberOfSidesToDraw(angle):
        return int(numberOfSides/360*angle)


def routePolygon(side, numberOfSidesToDraw):
    for i in range(numberOfSidesToDraw):
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


routeArc(130, 180+90)
turtle.mainloop()


