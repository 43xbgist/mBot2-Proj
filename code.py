import cyberpi as cpi
import time
#GLOBAL VARIABLES
distance = 300
line = 15
last_line = -1
over_line = 0
hi_p = 25
lo_p = 5
#FUNCTIONS
def get_all_values(output=True, black_line=True):
 global distance, line, over_line, hi_p, lo_p
 line = cpi.quad_rgb_sensor.get_line_sta(index = 1)
 if black_line: over_line = line < 15
 else: over_line = line > 0
 if output:
     cpi.console.println(str(line) + ' ' + str(distance))
def drive_lines():
global last_line
 if not last_line == line:
   last_line = line
   
 if line == 7: #L2
    cpi.mbot2.drive_power(lo_p, -hi_p) #turn left
 elif line == 11: #L1
  cpi.mbot2.drive_power(lo_p, -hi_p) #turn left
 elif line == 13: #R1
  cpi.mbot2.drive_power(hi_p, -lo_p) #turn right
 elif line == 14: #R2
  cpi.mbot2.drive_power(hi_p, -lo_p) #turn right
 elif line == 9: #L1 and R1
  cpi.mbot2.drive_power(hi_p, -hi_p) #straight ahead
#WAIT TO START
cpi.console.println('Press A')
while not cpi.controller.is_press('a'):
 cpi.led.on(255,0,0)
cpi.console.println('')
cpi.led.on(0,255,0)
#MAIN LOOP
cpi.mbot2.drive_power(20, -20)
while True:
 get_all_values(output=False, black_line=True)
 drive_lines()
