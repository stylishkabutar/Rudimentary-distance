'''
Constraints, bounds and objective for the model
'''
# Import necessary modules

import numpy as np
import pandas as pd
from d_config import BATTERY_CAPACITY, DISCHARGE_CAP, MAX_V,  MAX_CURRENT, BUS_VOLTAGE, HR,K
from d_car_dynamics import calculate_dx, calculate_power_req
from d_solar import calculate_incident_solarpower

# Define constants
SAFE_BATTERY_LEVEL = BATTERY_CAPACITY * DISCHARGE_CAP
MAX_P = BUS_VOLTAGE * MAX_CURRENT

# Bounds for the velocity
def get_bounds(N):
    '''
    Velocity bounds throughout the race
    '''
    return ([(0, 0)] + [(0.01, MAX_V)] * (N-2) + [(0, 0)]) # Start and end velocity is zero
#def control_stop_constraint(v,cumd):
    
   
    #if v[find_control_stops_v(v,cumd)]!=None:
 #   k=v[list(find_control_stops_v(v,cumd))]
    
  #  return -np.linalg.norm(-v[(find_control_stops_v(v,cumd))])
    #else:
     #   return 0

def objective(velocity_profile, dt, slope, InitialBatteryCapacity, FinalBatteryCapacity, wind_speed, wind_direction):
    '''
    Maximize total distance travelled
    '''
    dx = calculate_dx(velocity_profile[:-1], velocity_profile[1:], dt)
    #Min_B, B_bar = battery_and_acc_constraint(velocity_profile, dt, cum_d_array, slope_array, lattitude_array, longitude_array)

    # return np.abs(3055 * 10**3 - cum_d - np.sum(dx)) 
    discharge, overcharge, max_p, final_bat= battery_and_acc_constraint(velocity_profile, dt, slope, InitialBatteryCapacity, FinalBatteryCapacity, wind_speed, wind_direction)

    return - np.sum(dx) + 10 ** 10 * abs(final_bat) #+ np.max(-Min_B * 10 ** 16, 0) + np.max(-B_bar * 10 ** 12, 0)

def battery_and_acc_constraint(velocity_profile, dt, slope, InitialBatteryCapacity, FinalBatteryCapacity, wind_speed, wind_direction):
    '''
    Battery safety and acceleration constraint
    '''

    dx = calculate_dx(velocity_profile[:-1], velocity_profile[1:], dt)
    start_speeds, stop_speeds = velocity_profile[:-1], velocity_profile[1:]

    acceleration = (stop_speeds - start_speeds) / dt
    avg_speed = (start_speeds + stop_speeds) / 2
   

    # Find control stops
    cum_dtot = dx.cumsum()
    
    cum_dtot=cum_dtot / K
    P_req, _ = calculate_power_req(avg_speed, acceleration, slope, wind_speed, wind_direction)
    P_solar = calculate_incident_solarpower(dt.cumsum())
    energy_consumed = ((P_req - P_solar) * dt).cumsum()/HR
    battery_profile = InitialBatteryCapacity - energy_consumed - SAFE_BATTERY_LEVEL
    final_battery_lev = InitialBatteryCapacity - energy_consumed[-1] - FinalBatteryCapacity

    return np.min(battery_profile),(BATTERY_CAPACITY - SAFE_BATTERY_LEVEL) - np.max(battery_profile), MAX_P - np.max(P_req - P_solar),1000* final_battery_lev # Ensure battery level bounds
    
# def v_end(velocity_profile, dt, cum_d):
#     dx = calculate_dx(velocity_profile[:-1], velocity_profile[1:], dt)
#     d = cum_d + np.sum(dx)
#     return (3050 * 10 **3 - d) * np.min(velocity_profile), np.min(velocity_profile)
