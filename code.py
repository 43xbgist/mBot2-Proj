import cyberpi
left = 0
right = 0
reverse = False
def clamp_speed():
	left = max(0, min(left, 30))
	right = max(0, min(right, 30))
while True:
    if line == 7:
    	left -= 0.1
    	right -= 1
    	reverse = False
    elif line == 14:
    	left -= 1
    	right -= 0.1
    	reverse = False
    elif line == 15:
    	reverse = True
    else:
    	av = left + right
    	left = 1+(av/2)
    	right = left
    	reverse = False
    clamp_speed()
    if reverse:
    	cpi.mbot2.drive_power(-right, -left)
    else:
    	cpi.mbot2.drive_power(left, right)
