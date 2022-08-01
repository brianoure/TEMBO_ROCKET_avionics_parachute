import os
import time

current_absolute_altitude  = 0
previous_absolute_altitude = 0
current_pressure  = 0
previous_pressure = 0

"""DATA"""
def pressure():
    return 100000 #default
def altitude():
    return 1000 #default
def acceleration():
    return 0 #default
def gps():
    return 0 #default
"""DATA"""

def rocket_is_launched():
    launch_status = 1
    print("have we launched yet? ",launch_status)
    return launch_status

def deploy_parachute():
    print("GO GO parachute!")
    return 0

def altitude_is_decreasing():#by significant margin
    alt1 = altitude()
    time.sleep(1)
    alt2 = altitude()
    time.sleep(1)
    alt3 = altitude()
    time.sleep(1)
    alt4 = altitude()
    return ((alt2<alt1)and(alt4<alt3))

def pressure_is_increasing():#by significant margin
    pres1 = pressure()
    time.sleep(1)
    pres2 = pressure()
    time.sleep(1)
    pres3 = pressure()
    time.sleep(1)
    pres4 = pressure()
    return ((pres2>pres1)and(pres4>pres3))
   
try:
    runMAIN = True
    FLIGHT  = False
    while runMAIN:
        if( rocket_is_launched() ):
            FLIGHT = True
            while FLIGHT:
                if( altitude_is_decreasing() and pressure_is_increasing() ):#accel=0
                    deploy_parachute()
except:
    # what to do if a problem occurs!!!
    
