from cyberpi import *

if cyberpi.controller.is_press('a'):
    a = measureWall()
    cyberpi.console.print("The length of this wall is " + str(a) + " cm")


def measureWall():
    cyberpi.timer.reset()

    while True:
        distanceToWall = cyberpi.ultrasonic2.get(index=1)

        if distanceToWall < 15:
            cyberpi.mbot2.EM_stop(port="all")
            break
        else:
            cyberpi.mbot2.forward(speed=30)

    time = cyberpi.timer.get()
    wallLength = (20 * 0.3 * time) + 15
    return wallLength

def measureTurn(motorSpeedA, motorSpeedB, distanceToObstacle, time):
    angularDisplacementA = (motorSpeedA/100 * time)
    angularDisplacementB = (motorSpeedB/100 * time)
    averageAngularDisplacement = (angularDisplacementA + angularDisplacementB) / 2
    turnMeasurement = averageAngularDisplacement * distanceToObstacle

    return turnMeasurement
