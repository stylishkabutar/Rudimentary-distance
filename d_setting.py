'''
Set day-wise model parameters
'''

# Import necessary modules

from d_config import BATTERY_CAPACITY, KM, HR
import pandas as pd
import numpy as np
# Model Settings

ModelMethod = "COBYLA"
InitialGuessVelocity = 20 # m/s (Total average speed)

RunforDays = 5
# Day-wise race time

RACE_START = 8 * HR  # 8:00 am
RACE_END = 17 * HR  # 5:00 pm
FULL_DAY_TIME=RACE_END-RACE_START
# Race Parameters
RACE_DISTANCE = 3037 * KM
SLOPE=3
WIND_SPEED=3
WIND_DIRECTION=180
INITIAL_BATTERY_CAPACITY=BATTERY_CAPACITY
FINAL_BATTERY_CAPACITY=0
DT = RACE_END - RACE_START 

# Resolution 
STEP = 200 # s
# Average velocity

AVG_V = RACE_DISTANCE / (DT * RunforDays)
