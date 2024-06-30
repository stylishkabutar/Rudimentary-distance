'''
Run day-wise distance optimization model for multiple days
'''

# Import necessary modules
from d_setting import INITIAL_BATTERY_CAPACITY,FINAL_BATTERY_CAPACITY
from d_model import main



outdf, timetaken = main(INITIAL_BATTERY_CAPACITY, FINAL_BATTERY_CAPACITY) # Set day wise params
outdf.to_csv('raw_run_dat.csv', index=False)
print(f"Written data to `raw_run_dat.csv`")