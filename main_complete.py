import pandas as pd
import numpy as np

# Load the workout data
masked = pd.read_csv("C:/Users/Graduate/Desktop/Trackers (EXCEL)/tracker_weight/CBUM/CSV/Masked.csv")

def calculate_exercise_efforts():
    """
    Calculate effort for each exercise: Set1*Weight1 + Set2*Weight2 + Set3*Weight3 + Set4*Weight4
    Returns: exercise_names, exercise_efforts, total_efforts
    """
    exercise_names = []
    exercise_efforts = []
    total_efforts = []
    
    for i in range(masked.shape[0]):
        exercise_name = masked.iloc[i, 0]
        exercise_names.append(exercise_name)
        
        # Extract set and weight data
        set_1 = masked.iloc[i, 2]
        weight_1 = masked.iloc[i, 3]
        set_2 = masked.iloc[i, 4]
        weight_2 = masked.iloc[i, 5]
        set_3 = masked.iloc[i, 6]
        weight_3 = masked.iloc[i, 7]
        set_4 = masked.iloc[i, 8]
        weight_4 = masked.iloc[i, 9]
        
        # Handle NaN values - convert to 0
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
        
        # Calculate individual set efforts
        effort_1 = set_1 * weight_1
        effort_2 = set_2 * weight_2
        effort_3 = set_3 * weight_3
        effort_4 = set_4 * weight_4
        
        # Store individual efforts
        set_efforts = [effort_1, effort_2, effort_3, effort_4]
        exercise_efforts.append(set_efforts)
        
        # Calculate total effort for this exercise
        total_effort = effort_1 + effort_2 + effort_3 + effort_4
        total_efforts.append(total_effort)
        
        print(f"{exercise_name}: {total_effort}")
    
    return exercise_names, exercise_efforts, total_efforts

def get_unique_tags():
    """
    Extract unique muscle group tags from the data
    Returns: list of unique tags
    """
    unique_tags = masked.iloc[:, 1].dropna().unique().tolist()
    return unique_tags

def calculate_effort_by_tag():
    """
    Calculate total effort for each muscle group tag
    Returns: dictionary with tag as key and total effort as value
    """
    exercise_names, exercise_efforts, total_efforts = calculate_exercise_efforts()
    unique_tags = get_unique_tags()
    
    tag_efforts = {}
    
    for tag in unique_tags:
        tag_total = 0
        exercises_in_tag = []
        
        for i in range(len(exercise_names)):
            exercise_tag = masked.iloc[i, 1]  # Get tag for this exercise
            if exercise_tag == tag:
                tag_total += total_efforts[i]
                exercises_in_tag.append(exercise_names[i])
        
        tag_efforts[tag] = {
            'total_effort': tag_total,
            'exercises': exercises_in_tag,
            'exercise_count': len(exercises_in_tag)
        }
    
    return tag_efforts

def efforts_over_time():
    """
    Structure data for tracking efforts over time
    Currently time = 0, but structured for future time series
    Returns: dictionary with exercise data over time
    """
    exercise_names, exercise_efforts, total_efforts = calculate_exercise_efforts()
    
    time_series_data = {
        'time_period': 0,  # Current time period
        'exercises': {}
    }
    
    for i in range(len(exercise_names)):
        exercise_name = exercise_names[i]
        exercise_tag = masked.iloc[i, 1]
        
        time_series_data['exercises'][exercise_name] = {
            'tag': exercise_tag,
            'total_effort': total_efforts[i],
            'set_efforts': exercise_efforts[i],
            'time_period': 0
        }
    
    return time_series_data

def main():
    """
    Main function to run all calculations and display results
    """
    print("=== WORKOUT EFFORT ANALYSIS ===\n")
    
    # Calculate exercise efforts
    print("1. INDIVIDUAL EXERCISE EFFORTS:")
    print("-" * 40)
    exercise_names, exercise_efforts, total_efforts = calculate_exercise_efforts()
    
    print(f"\n2. EFFORT BY MUSCLE GROUP TAG:")
    print("-" * 40)
    tag_efforts = calculate_effort_by_tag()
    
    for tag, data in tag_efforts.items():
        print(f"{tag}: {data['total_effort']} (from {data['exercise_count']} exercises)")
        print(f"  Exercises: {', '.join(data['exercises'])}")
        print()
    
    print("3. EFFORTS OVER TIME (Current Period = 0):")
    print("-" * 40)
    time_data = efforts_over_time()
    
    print(f"Time Period: {time_data['time_period']}")
    print(f"Total Exercises: {len(time_data['exercises'])}")
    
    # Summary statistics
    total_workout_effort = sum(total_efforts)
    print(f"\n4. SUMMARY:")
    print("-" * 40)
    print(f"Total Workout Effort: {total_workout_effort}")
    print(f"Average Exercise Effort: {total_workout_effort / len(total_efforts):.2f}")
    print(f"Highest Effort Exercise: {exercise_names[total_efforts.index(max(total_efforts))]} ({max(total_efforts)})")
    print(f"Lowest Effort Exercise: {exercise_names[total_efforts.index(min(total_efforts))]} ({min(total_efforts)})")
    
    return {
        'exercise_data': list(zip(exercise_names, total_efforts)),
        'tag_data': tag_efforts,
        'time_data': time_data,
        'summary': {
            'total_workout_effort': total_workout_effort,
            'exercise_count': len(exercise_names),
            'tag_count': len(tag_efforts)
        }
    }

if __name__ == "__main__":
    results = main() 