import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(33, GPIO.OUT)
pins = dict()
pins = {29:0, 31:0}
def main():
	GPIO.output(33, GPIO.LOW)
	while True:
		pin1 = CheckPin(29)
		pin2 = CheckPin(31)
		if pin1 == 0:
			print("29 unpressed")
		if pin2 == 0:
			print("31 unpressed")
		if pin1 == 1:
			print("29 pressed")
		if pin2 == 1:
			print("31 pressed")

def SetLight(val):
	if(val == 0):
		GPIO.output(33, GPIO.LOW)
	else:
		GPIO.output(33, GPIO.HIGH)

def CheckPin(pin):
	returner = -1
	if(debouncedInput(pin) == False):
		if pins[pin] == 0:
			returner = 1
		pins[pin] = 1
	else:
		if pins[pin] == 1:
			returner = 0
		pins[pin] = 0
	return returner




def debouncedInput(pin):
	tries = 12
	i, ones,zeroes = 0,0,0
	while i < tries:
		bit = GPIO.input(pin)
		if(bit == 1):
			ones = ones + 1
			zeroes = 0
		else:
			zeroes = zeroes+1
			ones = 0
		i = i+1
		if ones>=3:
			return 1
		if(zeroes >=3):
			return 0
		time.sleep(0.01)
	print('bouncy input')
	return bit


if(__name__=='__main__'):
	main()
