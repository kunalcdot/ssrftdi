#from pyftdi.ftdi import Ftdi
from pyftdi.spi import SpiController

import time


# Instanciate a SPI controller
spi = SpiController()

# Configure the first interface (IF/1) of the FTDI device as a SPI master
spi.configure('ftdi://ftdi:4232h/2')

# Get a port to a SPI slave w/ /CS on A*BUS3 and SPI mode 0 @ 12MHz
slave = spi.get_port(cs=0, freq=1E6, mode=0)
slave.set_frequency(1000000)
print("wait 0.5sec")
print (slave.frequency)

time.sleep(0.5)
# Request the JEDEC ID from the SPI slave
#jedec_id = slave.exchange([0x9f,0xa5], 5).tobytes()
print("Data from slave = "),
#print (jedec_id)
time.sleep(0.5)


print("Sending read command\n")

print(slave.exchange([0x80],15).tobytes())	## read 5 bytes starting from add = 0x0



#slave.write(out=[0xa,0x11], start=True, stop=True)

#time.sleep(1)
#slave.write(out=[0xa0], start=False, stop=True)

spi.terminate()

#x = Ftdi()
#x.open_bitbang_from_url('ftdi:///1')

