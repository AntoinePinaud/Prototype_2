import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
ATMventilator_pin =  ...
GPIO.setup(ATMventilator_pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.output(ATMventilator_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(ATMventilator_pin, GPIO.LOW)
time.sleep(10)
GPIO.output(ATMventilator_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(ATMventilator_pin, GPIO.LOW)
