import numpy as np



#Normalize the data this will return the value between 0 and 1
def Normalization(x,overall_min,overall_max):
    #overall_min = 45 # specify the global minimun from all the datasets
    #overall_max = 800 # specify the global maximum from all the datasets
    x = (x - overall_min)/(overall_max - overall_min)
    
    return x

#To denormalize the data to original values from the normalized data
def De_Normalize(x,overall_min,overall_max):
    #overall_min = 45 # specify the global minimun from all the datasets
    #overall_max = 800 # specify the global maximum from all the datasets
    x = (x * (overall_max - overall_min) + overall_min)
    
    return x

