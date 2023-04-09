import network
import time
import urequests
from machine import Pin, Timer

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('***', '***')

led1 = Pin(13, Pin.OUT)
led2 = Pin(2, Pin.OUT)
timer = Timer()

def blink(timer):
    astronauts = urequests.get("https://h4r1ng9nzv56lyu.pocketbase.dev/api/collections/table/records/owbamvr7bktsq38").json()
    if astronauts['reserved'] == True:
        led1.high()
    else:
        led1.low()
                
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
