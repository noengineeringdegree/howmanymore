from gettext import npgettext
from IPython.display import display
import numpy as np 
import pandas as pd

masked = pd.read_csv("C:/Users/Graduate/Desktop/Trackers (EXCEL)/tracker_weight/CBUM/CSV/Masked.csv")


## interesting metrics to track
"""
Compare workouts: Track effort changes over time
Exercise ranking: See which exercises generate the most total effort
Progress tracking: Monitor effort increases across sessions
Export results: Save the calculated efforts to a new file
"""

def make_efforts_table():
    #calculates Set 1xWeight 1 for all exercises
    exercise_names = []  # Initialize the list
    all_efforts = []     # Initialize the list
    
    for i in range(masked.shape[0]):

        exercise_name = masked.iloc[i,0]
        exercise_names.append(exercise_name)  # Fixed typo

        set_1 = masked.iloc[i,2]
        weight_1 = masked.iloc[i,3]
        
        set_2 = masked.iloc[i,4]
        weight_2 = masked.iloc[i,5]

        set_3 = masked.iloc[i,6]
        weight_3 = masked.iloc[i,7]

        set_4 = masked.iloc[i,8]
        weight_4 = masked.iloc[i,9]

        # Debug: Print Bulgarian Split Squats data
        if exercise_name == "Bulgarian Split Squats":
            print(f"DEBUG - Raw data for {exercise_name}:")
            print(f"Set1: {set_1}, Weight1: {weight_1}")
            print(f"Set2: {set_2}, Weight2: {weight_2}")
            print(f"Set3: {set_3}, Weight3: {weight_3}")
            print(f"Set4: {set_4}, Weight4: {weight_4}")

        #handles NAs - convert to 0 if NaN, otherwise convert to float
        if pd.isna(set_1) or pd.isna(weight_1):
            set_1, weight_1 = 0.0, 0.0
        else:
            set_1, weight_1 = float(set_1), float(weight_1)
            
        if pd.isna(set_2) or pd.isna(weight_2):
            set_2, weight_2 = 0.0, 0.0
        else:
            set_2, weight_2 = float(set_2), float(weight_2)
            
        if pd.isna(set_3) or pd.isna(weight_3):
            set_3, weight_3 = 0.0, 0.0
        else:
            set_3, weight_3 = float(set_3), float(weight_3)
            
        if pd.isna(set_4) or pd.isna(weight_4):
            set_4, weight_4 = 0.0, 0.0
        else:
            set_4, weight_4 = float(set_4), float(weight_4)

        # Debug: Print processed data for Bulgarian Split Squats
        if exercise_name == "Bulgarian Split Squats":
            print(f"DEBUG - Processed data for {exercise_name}:")
            print(f"Set1: {set_1}, Weight1: {weight_1}")
            print(f"Set2: {set_2}, Weight2: {weight_2}")
            print(f"Set3: {set_3}, Weight3: {weight_3}")
            print(f"Set4: {set_4}, Weight4: {weight_4}")

        Exercises_Effort_1 = [i, set_1*weight_1]
        Exercises_Effort_2 = [i, set_2*weight_2]
        Exercises_Effort_3 = [i, set_3*weight_3]
        Exercises_Effort_4 = [i, set_4*weight_4]
        

        exercise_efforts = [Exercises_Effort_1, Exercises_Effort_2, Exercises_Effort_3, Exercises_Effort_4]
        all_efforts.append(exercise_efforts)

        effort_1 = exercise_efforts[0][1]  # Set1*Weight1
        effort_2 = exercise_efforts[1][1]  # Set2*Weight2  
        effort_3 = exercise_efforts[2][1]  # Set3*Weight3
        effort_4 = exercise_efforts[3][1]  # Set4*Weight4

        # Final NaN check before total calculation
        if pd.isna(effort_1): effort_1 = 0.0
        if pd.isna(effort_2): effort_2 = 0.0
        if pd.isna(effort_3): effort_3 = 0.0
        if pd.isna(effort_4): effort_4 = 0.0

        total_effort = effort_1 + effort_2 + effort_3 + effort_4  


        print(f"{exercise_name}")
        print(f"{total_effort}")
    
    return exercise_names, all_efforts

def extract_unique_tags_then_sum_by_tag():
    unique_tags = masked.iloc[:, 1].dropna().unique().tolist()
    print(f"{unique_tags}")
    
    return unique_tags

make_efforts_table()
unique_tags = extract_unique_tags_then_sum_by_tag()

