import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
NUTpump2_pin = ...                     #FloraGro
GPIO.setup(NUTpump2_pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.output(NUTpump2_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(NUTpump2_pin, GPIO.LOW)
time.sleep(10)
GPIO.output(NUTpump2_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(ANUTpump2_pin, GPIO.LOW)
