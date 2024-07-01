'''
Main day-wise model
'''

# Import necessary modules
import numpy as np
from scipy.optimize import minimize
import pandas as pd
from d_config import KM, HR, ModelMethod, InitialGuessVelocity, STEP,DT, SLOPE, WIND_SPEED, WIND_DIRECTION,INITIAL_BATTERY_CAPACITY,FINAL_BATTERY_CAPACITY
from d_car_dynamics import calculate_dx
from d_constraints import get_bounds, objective, battery_and_acc_constraint
from d_profiles import extract_profiles




step = STEP
N = DT // step
dt = np.full(int(N), step) # Set race time scale

 # Get data
   

N_V = int(N) + 1
    
initial_velocity_profile = np.concatenate((np.array([0]), np.ones(N_V - 2) * InitialGuessVelocity, np.array([0])))

bounds = get_bounds(N_V)

constraints = [
    {
            "type": "ineq",
            "fun": battery_and_acc_constraint,
            "args": (
                 dt, SLOPE, INITIAL_BATTERY_CAPACITY, FINAL_BATTERY_CAPACITY, WIND_SPEED, WIND_DIRECTION
            )
        }
     ]


print("Starting Optimisation")
   
optimised_velocity_profile = minimize(
        objective, 
        initial_velocity_profile,
        args = ( dt, SLOPE, INITIAL_BATTERY_CAPACITY, FINAL_BATTERY_CAPACITY, WIND_SPEED, WIND_DIRECTION),

        bounds = bounds,
        method = ModelMethod,
        constraints = constraints,
        options = {'catol': 10 ** -6, 'disp': True, 'maxiter': 2*10 ** 3}# "rhobeg":5.0}
        #options = {'maxiter': 3}
    )

optimised_velocity_profile = np.array(optimised_velocity_profile.x) * 1 # derive the velocity profile

dx = calculate_dx(optimised_velocity_profile[:-1], optimised_velocity_profile[1:], dt) # Find total distance travelled
distance_travelled = np.sum(dx) / KM # km

print("done.")
print(distance_travelled, "km in travel time:", dt.sum() / HR, 'hrs')

   
  
outdf = pd.DataFrame(
        dict(zip(
            ['Time', 'Velocity', 'Acceleration', 'Battery', 'EnergyConsumption', 'Solar', 'Cumulative Distance'],
            extract_profiles(optimised_velocity_profile, dt, SLOPE, INITIAL_BATTERY_CAPACITY, WIND_SPEED, WIND_DIRECTION)
        ))
    )
outdf['Cumulative Distance'] = np.concatenate([[0], dx.cumsum() / KM])
outdf.to_csv('run_dat.csv', index=False)
print("Written results to `run_dat.csv`")

    