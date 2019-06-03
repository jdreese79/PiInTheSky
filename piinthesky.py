import time
import datetime 
import math

import Adafruit_LSM303

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

lsm303 = Adafruit_LSM303.LSM303()

#f = open('piintheskydata.py' , 'w')

#f.write('Data')

#accel = lsm303.read()
#accel_y = accel
ydata = [1]
timedata = []

xIsZero = False
timereached = False
inLoop = True
Mytime = 0

start_time = time.time()

GPIO.output(18, GPIO.HIGH)
time.sleep(1)
GPIO.output(18, GPIO.LOW)
time.sleep(1)
GPIO.output(18, GPIO.HIGH)
time.sleep(1)
GPIO.output(18, GPIO.LOW)
time.sleep(1)

filename = "data" + str(datetime.datetime.now()) + ".txt"
print(filename)
f = open(filename, '+w')

while inLoop :
    if not xIsZero:
        
        f.write('Acceleration:')       
        
        data = lsm303.read()
        accel_y = data[0][1]
        time.sleep(.0001)
        ydata.append(str(accel_y))
        
        print(ydata)
        #s = ","
        #s = s.join(ydata)
        ydatastr = str(ydata)
        f.write(ydatastr)
        print(ydata[-2])
        g = int(ydata[-2])
        time.sleep(.0001)
        
    else:
        #Mytime = (0-((f)*elapsed_time))/(f)
        #start_time = time.time()
        #f = open('piintheskydata.txt' , 'w')

        f.write('Time')
        acceleration = g #ydata[-1]
        print('g')
        print(g) #(data[-1])
        
        elapsed_time = time.time() - start_time
        print('elapsed_time')
        print(elapsed_time)
        
        velocity = acceleration*elapsed_time
        print('velocity')
        print(velocity)
        
        Mytime = (0-((velocity)*elapsed_time))/(10)
        start_time2 = time.time()
        elapsed_time2 = time.time() - start_time2
        print('elapsed_time2')
        print(elapsed_time2)
        
        Mytime2 = abs(Mytime)
        print('mytime')
        print(Mytime2)
        
        timestr = str(Mytime2)
        f.write(timestr)
        f.close()
        #time.sleep(3)
       
        if (elapsed_time2 <= Mytime2):
            GPIO.output(18, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(18, GPIO.LOW)
            time.sleep(2)
            inLoop = False
            #f.close()
            #exit()
            #exit code
       # if elapsed_time == Mytime:
        #    GPIO.output(18, GPIO.HIGH)
         #   time.sleep(2)
          #  GPIO.output(18, GPIO.LOW)
           # sys.exit()
            
    
    #if accel_y == 0:
    if 10>= accel_y >= -10:
        xIsZero = True
    time.sleep(.5)
    
f.close()
GPIO.output(18, GPIO.HIGH)
time.sleep(.2)
GPIO.output(18, GPIO.LOW)
time.sleep(.2)
GPIO.output(18, GPIO.HIGH)
time.sleep(.2)
GPIO.output(18, GPIO.LOW)
time.sleep(.2)

#time.sleep(3)
        
        
#print('Time X={0}'.format(
#(0-(accel_y*elapsed_time))/(accel_y),))
        
        #while ( elapsed_time == (0-((data[0])*elapsed_time))/(data[0]) ):
            
          #  GPIO.output(18, GPIO.HIGH)
          #  sleep(1)
    
    
# vf = vi + at
# t = (vf-vi)/a
# t = (0-(accel_x*elapsed_time))/(accel_y)
