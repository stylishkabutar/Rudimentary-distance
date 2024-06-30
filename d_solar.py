'''
Solar power calculation
'''
import numpy as np

from d_config import PANEL_AREA, PANEL_EFFICIENCY
from d_setting import RACE_START, DT

def calc_solar_irradiance(time):
    '''
    Find Solar irradiance assuming Gausian distribution each day (temporary until solar data)
    '''
    return 1073.099 * np.exp(-0.5 * ((time - 43200) / 11600) ** 2)

def calculate_incident_solarpower(travel_time):
    '''
    Find instantanious solar power generated
    '''
    # gt = globaltime % DT # gives time spent on current day
    lt = RACE_START + travel_time # local time on current day
    intensity = calc_solar_irradiance(lt)
    return PANEL_AREA * PANEL_EFFICIENCY * intensity