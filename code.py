from cyberpi import *
import time 

#Global variables 
hi_pow=30
grad_pow = 15
low_pow= 10
rev_pow_s= -10
rev_pow_f= -25
line = 0
RBG_color = 0

def main_loop(): #drive the mBot2 by line sensor
    distanceToWall = ultrasonic2.get(index=1)
    line = quad_rgb_sensor.get_line_sta(index = 1) 
    if distanceToWall < 15:
        mbot2.EM_stop(port="all")
        measureQuarterTurn()
    else:
        if line == 15: 
            mbot2.drive_power(hi_pow, -hi_pow) # dirve straight 
        elif line == 14: 
            mbot2.drive_power(grad_pow, -hi_pow) # slow turn left 
            led.on(0,255,0) 
            time.sleep(1) 
        elif line == 13: 
            mbot2.drive_power(low_pow, -hi_pow) # slow turn left 
        elif line == 12: 
            mbot2.drive_power(rev_pow_s, -hi_pow) # slow turn left 
        elif line == 11: 
            mbot2.drive_power(hi_pow, -low_pow) # fast turn left 
        elif line == 10: 
            mbot2.drive_power(rev_pow_f, -rev_pow_s) # reverse turn left 
        elif line == 9: 
            mbot2.drive_power(rev_pow_f, -rev_pow_f) # reverse 
        elif line == 8: 
            mbot2.drive_power(rev_pow_f, -rev_pow_s) # reverse turn left 
        elif line == 7: 
            mbot2.drive_power(hi_pow, -grad_pow) # slow turn right 
        elif line == 6: 
            mbot2.drive_power(rev_pow_f, -rev_pow_f) # reverse 
        elif line == 5: 
            mbot2.drive_power(rev_pow_s, -rev_pow_f) # reverse turn right 
        elif line == 4: 
            mbot2.drive_power(rev_pow_s, -rev_pow_f) # reverse turn right 
        elif line == 3: 
            mbot2.drive_power(hi_pow, -rev_pow_s) # slow turn left 
        elif line == 1: 
            mbot2.drive_power(rev_pow_s, -rev_pow_f) # fast turn right 
        elif line == 0: 
            mbot2.drive_power(0, 0) # reverse 
        else:
            mbot2.drive_power(rev_pow_f, -rev_pow_f) # reverse 

def measureQuarterTurn():
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
        return None
    return turnMeasurement

#def break_lights(): 
     #if mbot2.drive_power == low_pow: 
     #  led.on(255,0,0) 
     #elif mbot2.drive_power == grad_pow: 
     #  led.on(255,0,0) 
     #elif mbot2.drive_power == rev_pow_s: 
     #  led.on(255,255,255) 
     #elif mbot2.drive_power == rev_pow_f: 
     #  led.on(255,255,255) 

console.println('Press A to start') 
while not controller.is_press('a'): 
    led.on(255,0,0) 
console.println('Starting...') 
time.sleep(1) 
console.println('Go, go, go!!!') 
console.println(str(RBG_color)) 
led.on(0,255,0) 
while True:
    main_loop()

