#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys

#init
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

# step for ear modes
ear_step = 0

# value range from 20 to 80, average of detected pixels from Lepton
position = 50

def run():
  global ear_step
  global position
  
  with open('action.txt') as f:
    action = f.readline()
  print action
  
  
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
    if isinstance(max_value, str):
      max_value = 400
    lines = f.readlines()

  thershold = 150

  img = []
  for line in lines:
    img.append(line.split())

  min_x = 0
  max_x = 80

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

  if action == "mode_aimed":
    fan.ChangeDutyCycle(40)

  if max_x == 80 and min_x == 0:
    position = 40
  else:
    position = 80 - (abs(max_x - min_x) / 2 + max_x)
  print "position: " + str(position)
  # the whisper to your ears mode
  if action == "mode_ears":
    ear_step += 1
    print ear_step

    if ear_step == 0:
      pass
    if ear_step == 1:
#     position = min(position + 40, 80)
      position = 80
    elif ear_step == 2:
      time.sleep(3)
      return # wait
    elif ear_step == 3:
      fan.ChangeDutyCycle(0)
      time.sleep(1)
      return
    elif ear_step == 4:
#      position = max(position - 40, 20)
      position = 0
    elif ear_step == 5:
      fan.ChangeDutyCycle(100)
      time.sleep(3)
      return
    elif ear_step == 6:
      fan.ChangeDutyCycle(0)
      time.sleep(1)
      return
    elif ear_step == 7:
      ear_step = 0
      return
    
    fan.ChangeDutyCycle(40)
  if action == "mode_strong":
    fan.ChangeDutyCycle(100)  

#  try:
  pwm = ((float(position) / 80.0) * 10.0 + 2.5)
  print "trying to move to pos: " + str(position) + ", pwm: " + str(pwm) + ", max_x: " + str(max_x) + ", min_x: " + str(min_x)
  pwm_x.ChangeDutyCycle(pwm)
#    print min_x, max_x, position, pwm
#  except:
#  print "missing values" + str(position) + str(max_x) + str(min_x)
#    pass
#  finally:
#    print max_value, thershold, min_x, max_x
  time.sleep(0.5)

while True:
  run()

