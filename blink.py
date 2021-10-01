import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
#frequency for PWM
f= 1
#pins 23,24,25 are connected to LEDs
LED1 = 23
LED2 = 16
LED3 = 25

#sets up LED pins as outputs
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

#sets up button pins as pull-down inputs
BUTTON1 = 5
BUTTON2 = 6
GPIO.setup(BUTTON1,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON2,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
print('All set up')

#defining callback function
def myCallback(turnOnLED):

  if turnOnLED == BUTTON1:
    pwm=GPIO.PWM(LED1, f)
    dc=0
    pwm.start(dc)
    #creating triangular waveform of 1 Hz
    for dc in range(101):
      pwm.ChangeDutyCycle(dc)
      sleep (0.005)
    for dc in range(101):
      pwm.ChangeDutyCycle(100-dc)
      sleep(0.005)
    pwm.stop()

  if turnOnLED == BUTTON2:
    pwm=GPIO.PWM(LED2, 1)
    dc=0
    pwm.start(dc)
    #creating triangular waveform of 1 Hz
    for dc in range(101):
      pwm.ChangeDutyCycle(dc)
      sleep (0.005)
    for dc in range(101):
      pwm.ChangeDutyCycle(100-dc)
      sleep(0.005)
    pwm.stop()
  

GPIO.add_event_detect(BUTTON1, GPIO.RISING, callback= myCallback, bouncetime=100)
GPIO.add_event_detect(BUTTON2, GPIO.RISING, callback= myCallback,bouncetime=100)

try:
  while True:
    print('the light is flashing')
    
    #LED3 is blinking constantly at 1Hz
    GPIO.output(LED3,0)
    sleep(0.5)
    GPIO.output(LED3,1)
    sleep(0.5)
except KeyboardInterrupt:
  print('\nExiting')
except Exception as e:
  print('\ne')

GPIO.cleanup()
