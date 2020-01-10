from m5stack import *
from m5ui import *
from uiflow import *
import wifiCfg
from m5mqtt import M5mqtt

setScreenColor(0x111111)


m5mqtt = M5mqtt('m5stick', 'io.adafruit.com', 1883, 'USER_NAME', 'YOUR_ACCESS_KEY', 300)

image0 = M5Img(0, 0, "res/humi3.jpg", True)

temperature = None
humidity = None
ticks = None


def fun_PATH_TO_TEMPERATURE_FEED_(topic_data):
  global temperature, humidity, ticks
  temperature = topic_data
  pass
m5mqtt.subscribe(str('PATH_TO_TEMPERATURE_FEED'), fun_PATH_TO_TEMPERATURE_FEED_)

def fun_PATH_TO_HUMIDITY_FEED_(topic_data):
  global temperature, humidity, ticks
  humidity = topic_data
  pass
m5mqtt.subscribe(str('PATH_TO_HUMIDITY_FEED'), fun_PATH_TO_HUMIDITY_FEED_)

def buttonA_wasPressed():
  global temperature, humidity, ticks
  axp.powerOff()
  pass
btnA.wasPressed(buttonA_wasPressed)

@timerSch.event('timer1')
def ttimer1():
  global temperature, humidity, ticks
  ticks = (ticks if isinstance(ticks, int) else 0) + 1
  pass


wifiCfg.doConnect('YOUR_WIFI_SSID', 'YOUR_WIFI_PASS')
m5mqtt.start()
temperature = '---'
humidity = '---'
ticks = 0
axp.setLDO2Volt(2.8)
setScreenColor(0x000000)
lcd.font(lcd.FONT_DejaVu24)
timerSch.run('timer1', 3500, 0x00)
while True:
  if ticks % 2 == 0:
    lcd.fill(0x000000)
    image0.changeImg("res/temp3.jpg")
    image0.setPosition(8, 8)
    lcd.print(temperature, 8, 80, 0xff6666)
  else:
    lcd.fill(0x000000)
    image0.changeImg("res/humi3.jpg")
    image0.setPosition(8, 8)
    lcd.print(humidity, 8, 80, 0x33ccff)
  wait_ms(3500)
  wait_ms(2)
