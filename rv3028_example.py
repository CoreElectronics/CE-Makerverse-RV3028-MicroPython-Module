from machine import I2C, Pin
import rv3028

#i2c = I2C(0, sda = Pin(0), scl = Pin(1))
i2c = I2C(0, sda=Pin(8), scl=Pin(9))
rtc = rv3028.rv3028(i2c = i2c)

print(rtc.timestamp()) 