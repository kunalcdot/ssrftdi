from pyftdi.ftdi import SpiController

#instanciate a SPI controller
spi = SpiController()

# Configure the first interface (IF/1) of the FTDI device as a SPI master


spi.configure('ftdi://ftdi:4232h/1')

# Get a port to a SPI slave w/ /CS on A*BUS3 and SPI mode 0 @ 12MHz
slave = spi.get_port(cs=0, freq=12E6, mode=0)

# Request the JEDEC ID from the SPI slave
jedec_id = slave.exchange([0x9f], 3).tobytes()
print("hello")

