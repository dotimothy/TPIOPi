import os
import time 

print("RPi CPU Clock Measurer\n")

while True:
	os.system("vcgencmd measure_clock arm")
	time.sleep(0.1)
