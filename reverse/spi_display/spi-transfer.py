#!/usr/bin/env python
import Adafruit_BBIO.SPI as SPI
 
from Adafruit_BBIO.SPI import SPI


# This opens the 2nd SPI interface which is SPI1 on the board, or /dev/SPI2.0 - with CSO
spi = SPI(2, 0)

# This sets the bit rate to 100kbps
spi.msh=100000

# The number of bits / word
spi.bpw=8

# xfer2 function holds the CS line until all the data is transmitted.
# The function will return data received
#   if there is a physical loopback you'll between MISO and MOSI you'll see the same characters printed as sent
# If there is no loopback, you'll likely see 0xffs or 255s printed (all high)
print(spi.xfer2([0x76,0x79,0x01,0x08]))

# xfer function releases and reactivats the CS line between blocks transmitted
# The additional argument is the delay between blocks transmitted.
# print(spi.xfer([0x76, 0x79, 0x01, 0x08],1000))



spi.close()
