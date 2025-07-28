from gettext import npgettext
from IPython.display import display
import numpy as np 
import pandas as pd

workout_sheet = pd.read_csv(r"C:\Users\Graduate\Desktop\Trackers (EXCEL)\CBUM\CSV\Leg.csv")

workout_sheet_headers = workout_sheet.columns[1]
# If you know the column names
column_names = workout_sheet.columns[1:4].tolist()
set_1 = workout_sheet.columns[2,3].tolist()
set_2 = workout_sheet.columns[4,5].tolist()
set_3 = workout_sheet.columns[6,7].tolist()
set_4 = workout_sheet.columns[8,9].tolist()

def get_tags(column):
    return column.dropna().unique().tolist()

# Get the second column and convert to tags
tags = get_tags(workout_sheet.iloc[:, 1])
print(tags)

def store_efforts(efforts):
    effort_array = []
    for effort in efforts:
        if not
            return []
        if 