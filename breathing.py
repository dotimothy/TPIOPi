import RPi.GPIO as GPIO
import time

led = 11 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
pwm = GPIO.PWM(led, 100)
pwm.start(0)
while(True):
	for i in range(0,100):
		pwm.ChangeDutyCycle(i)
		time.sleep(0.005)
	for j in range(100,0,-1):
		pwm.ChangeDutyCycle(j)
		time.sleep(0.005)
pwm.stop()
GPIO.cleanup()

