'''
Configure data
'''
import numpy as np
import pandas as pd
#---------------------------------------------------------------------------------------------------------------
# Unit conversions

K = 10 ** 3 
KM = 10 ** 3 # m
MM = 10 ** (-3) # m
DAY = 86400 # s
HR = 3600 # s
# ----------------------------------------------------------------------------

# Car data

# Physical attributes

INNER_WHEEL_RADIUS = 0.214 # m
OUTER_WHEEL_RADIUS = 0.2785 # m
CAR_MASS = 260 # kg
NO_OF_WHEELS = 3
FRONTAL_AREA = 1 # m^2


# Battery

BATTERY_CAPACITY = 3.055 * K # Wh
DISCHARGE_CAP = 0.2 # Below this fraction of battery -> deep discharge

# Motor

STATOR_ROTOR_AIR_GAP = 1.5 * MM # m

# Solar Panel

PANEL_AREA = 6 # m^2
PANEL_EFFICIENCY = 0.19

# Bus voltage

BUS_VOLTAGE = 4.2 * 38*1 # V

# Low voltage loss

POWER_LV = 100 # watts

#-------------------------------------------------------------------------------------------

# Resistance

CD = 0.092
CDA = 0.093 # Drag Area = Aerodynamic coefficient * Fronal area
ZERO_SPEED_CRR = 0.005 

# Other constants

AIR_DENSITY = 1.192 # kg/m^3
GRAVITY = 9.81 # m/s^2
AIR_VISCOSITY = 1.524 * 10 ** (-5) # Pa.s (Kinematic viscosity of air)
AMBIENT_TEMP = 295 # K 

# Constraints

MAX_V = 35 # m/s
MAX_CURRENT = 12.3 # A

# Race config

RACE_DISTANCE = 3047 # km
RACE_START = 8 * HR  # put starting time
RACE_END = 17 * HR  # ending time
RACE_TIME=RACE_END-RACE_START

#-------------------------------------------------------------------------------------------

# Configurable parameters

#Optimization Parameters
ModelMethod = "COBYLA"
InitialGuessVelocity = 20 # m/s (Total average speed)
STEP = 200 # s

# Track and Environment
SLOPE=0
WIND_SPEED=3
WIND_DIRECTION=180

#Battery characteristics
INITIAL_BATTERY_CAPACITY=BATTERY_CAPACITY
FINAL_BATTERY_CAPACITY=0
DT = RACE_END - RACE_START 

# Average velocity

AVG_V = RACE_DISTANCE /RACE_TIME
# ---------------------------------------------------------------------------------------------