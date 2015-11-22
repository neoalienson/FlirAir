#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys

fname = 'output.pgm'


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
pwm_x = GPIO.PWM(11, 50)
pwm_x.start(7.5)

GPIO.setup(7, GPIO.OUT)
pwm_y = GPIO.PWM(7, 50)
pwm_y.start(7.5)

GPIO.setup(12, GPIO.OUT)
fan = GPIO.PWM(12, 25)
fan.start(0)


def run():
  with open('action.txt') as f:
    action = f.readline()
  print action
  
  if action == "mode_aimed":
    fan.ChangeDutyCycle(40)
  if action == "mode_ears":
    fan.ChangeDutyCycle(40)
  if action == "mode_strong":
    fan.ChangeDutyCycle(100)  
  
  if action == "head":
    pwm_y.ChangeDutyCycle(9)
  if action == "torso":
    pwm_y.ChangeDutyCycle(7.5)
  if action == "legs":
    pwm_y.ChangeDutyCycle(6)  
  
  with open(fname) as f:
    f.readline()
    f.readline()
    max_value = f.readline()
    lines = f.readlines()

  thershold = 150

  img = []
  for line in lines:
    img.append(line.split())

  min_x = 0
  max_x = max_value * 2

  if len(img) >= 60:
    for y in range(20):
      if len(img[y]) >= 80:
        for x in range(80):
          val = img[y][x]
          if float(val) > thershold:
            sys.stdout.write('#')
            min_x = max(min_x, x)
            max_x = min(max_x, x)
          else:
            sys.stdout.write('.')
      else:
        print "out of range in img x: "
        print len(img[y])
      print '|'
  else:
    print "out of range in img y"

  try:
    position = min_x + max_x / 2
    pwm = (80 - position) * 10 / 80 + 4
    pwm_x.ChangeDutyCycle(pwm)
    print position
#    print min_x, max_x, position, pwm
  except:
    pass
#  finally:
#    print max_value, thershold, min_x, max_x
  time.sleep(2)

while True:
  run()

