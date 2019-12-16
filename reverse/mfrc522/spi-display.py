#!/usr/bin/env python
import Adafruit_BBIO.SPI as SPI 
from Adafruit_BBIO.SPI import SPI
from time import sleep as delay

def DisplayFirstLED(a,b,c,d):
	spi = SPI(2, 0)
	spi.msh=100000
	spi.bpw=8
	print(spi.xfer2([0x76,0x79,0x00,a,b,c,d]))
	delay(0.001)
	spi.close()
	return

def DisplaySecondLED(a,b,c,d):
        spi = SPI(2, 1)
        spi.msh=100000
        spi.bpw=8
        print(spi.xfer2([0x76,0x79,0x00,a,b,c,d]))
        delay(0.001)
        spi.close()
        return

for number in reversed(range(9999)):
	NumToDigit=str(number).zfill(4)
	a=int(NumToDigit[0])
	b=int(NumToDigit[1])
	c=int(NumToDigit[2])
	d=int(NumToDigit[3])
	DisplayFirstLED(a,b,c,d)
	DisplaySecondLED(a,b,c,d)



"""
spi = SPI(2, 0)
spi.msh=100000
spi.bpw=8
print(spi.xfer2([0x76,0x79,0x01,0x9]))
spi.close()

spi = SPI(2, 1)
spi.msh=100000
spi.bpw=8
print(spi.xfer2([0x76,0x79,0x01,0x01]))
spi.close()

"""
