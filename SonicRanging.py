import pigpio
import time

def pulseLn(pin, timeOut):
    intTime = time.time()
    while(pi.read(pin) == 0):
        if((time.time()-intTime > timeOut) * .000001):
            return 0
    
    intTime = time.time()
    while(pi.read(pin) == 1):
        if((time.time()-intTime) > timeOut * .000001):
            return 0
        
    pulseTime = (time.time() - intTime) * 1000000
    return pulseTime


def getDist():
    pi.gpio_trigger(TRIG_PIN, 10, 1)
    pingTime = pulseLn(ECHO_PIN, timeOut)
    distance = pingTime * 340.0 / 2.0 / 10000.0
    return distance

pi = pigpio.pi()

ECHO_PIN = 21
TRIG_PIN = 20

maxDistance = 400 #cm
timeOut = maxDistance*60

pi.set_mode(ECHO_PIN, pigpio.INPUT)
pi.set_mode(TRIG_PIN, pigpio.OUTPUT)

try:
    while(True):
        print("Distance: " , getDist()/2.54, "in")
        time.sleep(1)
except:
    pi.stop
    print("Stopped")