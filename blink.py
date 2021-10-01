import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
#pin 25 will be blinking
p= 24
#f= 1
#dc= 50
GPIO.setup(p, GPIO.OUT)

while True:
  GPIO.output(p,0)
  sleep(0.5)
  GPIO.output(p,1)
  sleep(0.5)
'''
#pwm = GPIO.PWM(print)

try:
  pwm.start(dc)
  while True:
    pass
except KeyboardInterrupt:
  print('\nExiting')


pwm.stop()
GPIO.cleanup()
'''