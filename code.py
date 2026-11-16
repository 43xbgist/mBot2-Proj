from cyberpi import *
left = 0
right = 0
reverse = False
def clamp_speed():
	left = max(0, min(left, 30))
	right = max(0, min(right, 30))
while True:
	left = (quad_rgb_sensor.get_offset_track(index = 1)*0.3) + 20
	right = (quad_rgb_sensor.get_offset_track(index = 1)*0.3) + 20
    clamp_speed()
    if reverse:
    	mbot2.drive_power(right, -left)
    else:
    	mbot2.drive_power(-left, right)
