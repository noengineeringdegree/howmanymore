from gettext import npgettext
from IPython.display import display
import numpy as np 
import pandas as pd

masked = pd.read_csv("C:/Users/Graduate/Desktop/Trackers (EXCEL)/tracker_weight/CBUM/CSV/Masked.csv")

workout_sheet_headers = masked.columns[1]
# If you know the column names
column_names = masked.columns[1:4].tolist()
set_1 = masked.columns[2:4].tolist()
set_2 = masked.columns[4:6].tolist()
set_3 = masked.columns[6:8].tolist()
set_4 = masked.columns[8:10].tolist()

def get_tags(column):
    return column.dropna().unique().tolist()

# Get the second column and convert to tags
tags = get_tags(masked.iloc[:, 1])
print(tags)

def store_efforts(efforts):
    effort_array = []
    for effort in efforts:
        if not effort:
            return []
        if effort > 0:
            effort_array.append(effort)
    return effort_array 