import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
####### Lighting module (LIG)
LIGled_pin = ...
GPIO.setup(LIGled_pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.output(LIGled_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(LIGled_pin, GPIO.LOW)
time.sleep(10)
GPIO.output(LIGled_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(LIGled_pin, GPIO.LOW)
