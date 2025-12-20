# Building retention curve through logarithmic-linear interpolation imputing for not known days. (D0, D2, D3, D5, D6, D8, ... D15)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def retention_curve(d1, d3, d7, d14, maximum=30):

    """
    This functions as exponentially decay retention over time. 
    This looks the correct method because retention in mobile games is most likely exponentially decay.

    - D0 retention assumed as 1.0 because the user downloads counted as 1 and likely play the game after downloaded.   
    - Retention ratios assigned to parameters ; d1, d3, d7, d14 as float data type. 
    - maximum : This parameters works as the last day of retention according to the c), d), e) questions. Data type is integer. 


    """
    
    known_days = np.array([0,1,3,7,14])
    reten_rates = ([1.0, d1, d3, d7, d14])
    
    # D1, D3, D7 and D14 are known retention points. The reason for (max + 1) is python language not includes the second parameter to the interval. 
    # Starts from 0 to the max - 1 so we add + 1 to achieve max.
    reten_days = np.arange(0, maximum + 1)
    
    # Logarithmic-linear interpolation

    """
    This method is based on from a pure mathematical model. Since the decay is exponentially and we want to predict the retention days:
    
    R(t) = A. e ^ -kt

    R(t) = Active users for t th day
    A = Starting point (D0 = 1)
    k = Chrun rate

    When we take logarithms of parameters on the function: log(R(t)) = log(A) - kt  
    
    """
    
    log_reten_known = np.log(reten_rates)
    
    # np.interp method predicting the log-rates as linearly for the retention points   
    log_reten_days = np.interp(reten_days, known_days, log_reten_known)
    
    # Go back to the first retention points
    reten_back  = np.exp(log_reten_days)

    # We do not have the data for after 14 days retention points. So, assuming that the decay goes down as we decied:    
    slope = (np.log(d14) - np.log(d7)) / 7

    
    for day in range(15, maximum + 1):
        reten_back[day] = np.exp(np.log(d14) + slope * (day - 14))

    return pd.Series(reten_back, index=reten_days, name="retention")




