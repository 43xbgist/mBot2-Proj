from cyberpi import *

if controller.is_press('a'):
    a = measureWall()
    console.print("The length of this wall is " + str(a) + " cm")


def measureWall():
    timer.reset()

    while True:
        distanceToWall = ultrasonic2.get(index=1)

        if distanceToWall < 15:
            mbot2.EM_stop(port="all")
            break
        else:
            mbot2.forward(speed=30)

    time = timer.get()
    wallLength = (20 * 0.3 * time) + 15
    return wallLength

def measureQuarterTurn():

    mbot2.backward(speed=30, duration=2)

    distanceToObstacle = ultrasonic2.get(index=1)

    motorSpeedB = 15
    motorSpeedA = motorSpeedB * ((distanceToObstacle + 4) / (distanceToObstacle - 4))

    time = (3.14159 * 8) / (2 * (motorSpeedA - motorSpeedB))

    timer.reset()
    while timer.get() < time:
        mbot2.drive_speed(motorSpeedA, motorSpeedB)

    mbot2.EM_stop(port="all")

    angularDisplacementA = (motorSpeedA/100 * time)
    angularDisplacementB = (motorSpeedB/100 * time)
    averageAngularDisplacement = (angularDisplacementA + angularDisplacementB) / 2
    turnMeasurement = averageAngularDisplacement * distanceToObstacle

    console.print(turnMeasurement)

    if ultrasonic2.get(index=1) >= 12:
        mbot2.forward(speed=30, duration=2)
    else:
        console.print("Turn not possible")
        return None

    return turnMeasurement
