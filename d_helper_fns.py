from d_config import KM
from d_setting import RACE_DISTANCE
def find_reachtime(cum_dt, cum_d):
    '''
    Find time at which race distance is crossed
    '''
    for i  in range(len(cum_d)):
        if cum_d[i] > (RACE_DISTANCE / KM):
            return cum_dt[i]
    return cum_dt[-1]