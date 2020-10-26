# M5stickC battery current and voltage
from m5stack import *
from m5ui import *
from uiflow import *
lcd.setRotation(3)

setScreenColor(0x000000)
axp.setLDO2Volt(2.7)
lcd.clear()
while True:
  lcd.font(lcd.FONT_DefaultSmall)
  lcd.print('battery voltage', 0, 0, 0x330099)
  lcd.font(lcd.FONT_DejaVu24)
  lcd.print(((str(("%.2f"%((axp.getBatVoltage())))) + str(' '))), 0, 14, 0x33ffff)
  lcd.font(lcd.FONT_DejaVu18)
  lcd.print('V', 100, 18, 0x3333ff)
  lcd.font(lcd.FONT_DefaultSmall)
  lcd.print('battery current', 0, 40, 0x330099)
  lcd.font(lcd.FONT_DejaVu24)
  lcd.print(((str(("%.1f"%((axp.getBatCurrent())))) + str('   '))), 0, 54, 0x33ffff)
  lcd.font(lcd.FONT_DejaVu18)
  lcd.print('mA', 100, 58, 0x3366ff)
  wait_ms(2)
