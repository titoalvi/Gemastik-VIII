import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT)

while True:
	gpio.output(7,gpio.LOW)             

