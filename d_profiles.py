import numpy as np
import pandas as pd
from d_config import BATTERY_CAPACITY, HR, K
from d_car_dynamics import calculate_power_req, calculate_dx
from d_solar import calculate_incident_solarpower


def extract_profiles(velocity_profile, dt, slope, InitialBatteryCapacity, wind_speed, wind_direction):
    # convert data to time domain
    start_speeds, stop_speeds = velocity_profile[:-1], velocity_profile[1:]
    avg_speed = (start_speeds + stop_speeds) / 2
    acceleration = (stop_speeds - start_speeds) / dt
    dx = calculate_dx(start_speeds, stop_speeds, dt)
    P_req, _ = calculate_power_req(avg_speed, acceleration, slope, wind_speed, wind_direction)
    P_solar = calculate_incident_solarpower(dt.cumsum())

    energy_consumption = P_req * dt / HR # Wh


    energy_gain = P_solar * dt 

    energy_gain1 = energy_gain
    energy_gain = energy_gain / HR 
    net_energy_profile = energy_consumption.cumsum() - energy_gain.cumsum()

    battery_profile = InitialBatteryCapacity - net_energy_profile
    battery_profile = np.concatenate((np.array([InitialBatteryCapacity]), battery_profile))

    battery_profile = battery_profile * 100 / (BATTERY_CAPACITY)
    dt =  np.concatenate((np.array([0]), dt))
    energy_gain = np.concatenate((np.array([np.nan]), energy_gain))
    energy_gain1 = np.concatenate((np.array([np.nan]), energy_gain1))
    energy_consumption =  np.concatenate((np.array([np.nan]), energy_consumption))
    acceleration = np.concatenate((np.array([np.nan]), acceleration,))
    dx = np.concatenate((np.array([0]), dx))
    
    return [
        dt.cumsum(),
        velocity_profile,
        acceleration,
        battery_profile,
        energy_consumption,
        energy_gain1 / HR,
        dx,
    ]