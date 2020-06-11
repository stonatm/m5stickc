from m5stack import *
from m5ui import *
from uiflow import *
import time
import machine

setScreenColor(0x000000)




label0 = M5TextBox(0, 4, "average power", lcd.FONT_Default,0xFFFFFF, rotate=0)
image0 = M5Img(0, 40, "res/bulb_of.jpg", True)
label1 = M5TextBox(0, 149, "0", lcd.FONT_DefaultSmall,0xffffff, rotate=0)

from numbers import Number

power = None
ticks = None
IMP_PER_KWH = None


@timerSch.event('timer1')
def ttimer1():
  global power, ticks, IMP_PER_KWH
  M5Led.on()
  wait_ms(5)
  M5Led.off()
  power = (ticks * 1000) / (IMP_PER_KWH / 60)
  label0.setText(str((str(int(power)) + str(' W'))))
  ticks = 0
  label1.setText(str(ticks))
  pass


setScreenColor(0x000000)
image0.setPosition(0, 40)
label0.setPosition(0, 4)
label0.setColor(0xffcc00)
label0.setFont(lcd.FONT_DejaVu18)
label1.setPosition(0, 150)
label1.setColor(0x33cc00)
label1.setFont(lcd.FONT_DefaultSmall)
pin0 = machine.Pin(36, mode=machine.Pin.IN, pull=machine.Pin.PULL_FLOAT)
IMP_PER_KWH = 6400
ticks = 0
power = 0
timerSch.run('timer1', 60000, 0x00)
while True:
  if not (pin0.value()):
    image0.changeImg("res/bulb_on.jpg")
    while not (pin0.value()):
      pass
    ticks = (ticks if isinstance(ticks, Number) else 0) + 1
    label1.setText(str(ticks))
  else:
    image0.changeImg("res/bulb_of.jpg")
  wait_ms(2)
