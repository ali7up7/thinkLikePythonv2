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

def routeZ(z):
    z.fd(100)
    z.rt(135)
    z.fd(int(100 * math.sqrt(2)))
    z.lt(135)
    z.fd(100)





