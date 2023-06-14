from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from datetime import datetime
import time

import urllib.request
import requests
import urllib
from urllib.request import urlopen
import urllib3


serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=90, blocks_arranged_in_reverse_order=True)
device.contrast(4)

#for line in urllib.request.urlopen('https://pierrevauchel.fr/msg.txt'):
#	msg = line.decode('utf-8')

#msg = "HELLO"

while True:

    with open('/var/www/html/msg.txt', 'r') as f:
        msg = f.read()
    length = len(msg)
    length = (length*8)
    
    for x in range(32, -length, -1):
        
        with canvas(device) as draw:
            text(draw, (x, 0), msg, fill="white", font=proportional(TINY_FONT))
        time.sleep(0.10)
    time.sleep(0.2)
