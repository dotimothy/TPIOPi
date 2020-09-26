try:
	import RPi.GPIO as GPIO
except ModuleNotFoundError: 
	print("You don't have GPIO Pins, so you can't run this program!"),
	exit()
	
import time

led = input("Welcome!\nPlease specify the pin you have connected to via \"+\" terminal: ")
print("\nYou have selected pin " + str(led) + " to setup.\n")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)

cycle = input("Please specify duration of the led cycle (in seconds): ")
print("\nYour LED Cycle is " + str(cycle) + " second(s)\n")
time.sleep(1)

while True:
	print("LED On")
	GPIO.output(led,True)
	time.sleep(cycle)
	print("LED Off")
	GPIO.output(led, False)
	time.sleep(cycle)
GPIO.cleanup()
