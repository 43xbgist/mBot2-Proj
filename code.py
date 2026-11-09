import cyberpi
#add imports up here


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
 
    cyberpi.console.print("The length of this wall is " + str(wallLength) + " cm") 

 


while True:
    if cyberpi.controller.is_press('a'): 
    measureWall() 

 
