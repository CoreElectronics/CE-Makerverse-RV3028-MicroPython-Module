from machine import I2C, Pin
from Makerverse_RV3028 import Makerverse_RV3028

#i2c = I2C(0, sda = Pin(0), scl = Pin(1))
i2c = I2C(0, sda=Pin(8), scl=Pin(9))
rtc = Makerverse_RV3028(i2c = i2c)

print(rtc.timestamp()) 
