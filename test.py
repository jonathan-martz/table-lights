import network
import time
import urequests
from machine import Pin, Timer

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('JM - Multimedia', '?EsLeuchtetBlau!')

red = Pin(13, Pin.OUT)
green = Pin(2, Pin.OUT)
timer = Timer()

def blink(timer):
    table = urequests.get("https://h4r1ng9nzv56lyu.pocketbase.dev/api/collections/table/records/owbamvr7bktsq38").json()
    if (table['reserved'] == True) or (table['used'] == True):
        red.high()
        green.low()
        
        if table['reserved'] == True:
            print('Reserviert');
        if table['used'] == True:
            print('Benutzt');
    else:
        green.high()
        red.low();
blink(timer)               
#timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)

