import os
import time 

print("RPi Temp Measurer\n")

while True:
	os.system("vcgencmd measure_temp")
	time.sleep(0.1)
