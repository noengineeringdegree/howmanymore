from gettext import npgettext
from IPython.display import display
import numpy as np 
import pandas as pd

masked = pd.read_csv("C:/Users/Graduate/Desktop/Trackers (EXCEL)/tracker_weight/CBUM/CSV/Masked.csv")


def make_efforts_table():
    #calculates Set 1xWeight 1 for all exercises
    exercise_names = []  # Initialize the list
    all_efforts = []     # Initialize the list
    
    for i in range(masked.shape[0]):

        exercise_name = masked.iloc[i,0]
        exercise_names.append(exercise_name)  # Fixed typo

        set_1 = masked.iloc[i,2]
        weight_1 = masked.iloc[i,3].astype(float)
        
        set_2 = masked.iloc[i,4]
        weight_2 = masked.iloc[i,5].astype(float)

        set_3 = masked.iloc[i,6]
        weight_3 = masked.iloc[i,7].astype(float)

        set_4 = masked.iloc[i,8]
        weight_4 = masked.iloc[i,9].astype(float)

        Exercises_Effort_1 = [i, set_1*weight_1]
        Exercises_Effort_2 = [i, set_2*weight_2]
        Exercises_Effort_3 = [i, set_3*weight_3]
        Exercises_Effort_4 = [i, set_4*weight_4]
        

        exercise_efforts = [Exercises_Effort_1, Exercises_Effort_2, Exercises_Effort_3, Exercises_Effort_4]
        all_efforts.append(exercise_efforts)

        effort_1 = exercise_efforts[0][1]  # Set1*Weight1
        effort_2 = exercise_efforts[1][1]  # Set2*Weight2  
        effort_3 = exercise_efforts[2][1]  # Set3*Weight3
        effort_4 = exercise_efforts[3][1]# Set4*Weight4

        total_effort = effort_1 + effort_2 + effort_3 + effort_4  
        

        print(f"{exercise_name}")
        print(f"{total_effort}")
    
    return exercise_names, all_efforts, total_effort

# Call the function
make_efforts_table()
