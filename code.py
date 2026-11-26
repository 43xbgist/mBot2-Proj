from cyberpi import *
import time 
import math

left = 0
right = 0

#Speed settings
speed = 20
rotate = 30

#LED colours
finish = [55, 255, 55]
standby = [255, 80, 0]
search = [0, 111, 255]
indicate = [255, 200, 0]
reverse = [250, 250, 200]


def main_loop(): # ----- MAIN LOOP ----- #
    distanceToWall = ultrasonic2.get(index = 1)
    if distanceToWall < 15:
        mbot2.drive_power(0,0)
        wall()
    else: # ----- MOVEMENT ----- #
        left = speed
        right = speed
        if quad_rgb_sensor.is_background("L2", index = 1):
            right *= 0.5
            if quad_rgb_sensor.is_background("L1", index = 1):
                right *= -2
        if quad_rgb_sensor.is_background("R2", index = 1):
            left *= 0.5
            if quad_rgb_sensor.is_background("R1", index = 1):
                left *= -2
        if left<0 and right<0:
            led.on(reverse[0], reverse[1], reverse[2])
        else:
            led.on(0,0,0)
        if left<right:
            led.on(indicate[0], indicate[1], indicate[2], id=1)
        if right<left:
            led.on(indicate[0], indicate[1], indicate[2], id=5)
        mbot2.drive_power(left,-right)


def wall(): # ----- OBSTACAL AVOIDENCE ----- #
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

    if ultrasonic2.get(index=1) <= 12:
        console.print("Turn not possible")


while True: # ----- SETUP LOOP ----- #
    console.println('Press B to start')
    t=0
    while not controller.is_press('b'):# plays an animation until pressed
        time.sleep(0.01)
        l=math.pow(math.sin(math.pi*t),2)
        led.on(standby[0]*l, standby[1]*l, standby[2]*l)
        t+=0.01
    console.clear()
    console.println('Starting...')
    time.sleep(1)
    console.println('Go, go, go!!!')
    t=time.time()
    while True: # ----- EXTERNAL LOOP ----- #
        if time.time() > t + 5:# Clear text after 5s
            console.clear()
        if controller.is_press('a'):# Pausing
            console.clear()
            console.println("Paused.")
            mbot2.drive_power(0,0)
            break
        elif quad_rgb_sensor.is_color("y", "any", index = 1):# Goal condition
            mbot2.drive_power(0,0)
            console.clear()
            console.println("Finished!") 
            t=0
            while True:
                time.sleep(0.01)
                l=math.pow(math.sin(math.pi*t),2)
                led.on(finish[0]*l, finish[1]*l, finish[2]*l)
                t+=0.01
        else:
            main_loop()
