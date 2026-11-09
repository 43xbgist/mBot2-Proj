import cyberpi
#add imports up here
last_vel = 0

def change_speed(set):
	if set<last_vel:
		cyberpi.led.on(255, 0, 0, id = "all")
	else:
		cyberpi.led.off(id = "all")
	last


while True:
  print("Hello World")
