try:
	import RPi.GPIO as GPIO
except ModuleNotFoundError: 
	print("You don't have GPIO Pins, so you can't run this program!"),
	exit()

led = 11 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
pwm = GPIO.PWM(led, 100)
pwm.start(0)
while(True):
	brightness = input("How Bright?\n")
	pwm.ChangeDutyCycle(brightness)
pwm.stop()
GPIO.cleanup()

