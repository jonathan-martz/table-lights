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
    astronauts = urequests.get("https://tl.jmartz.gmbh/api/tisches/1").json()
    if astronauts['data']['attributes']['reserviert'] == True:
        led1.high()
    else:
        led1.low()
        
    if astronauts['data']['attributes']['frei'] == True:
        led2.high()
    else:
        led2.low()
        
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
