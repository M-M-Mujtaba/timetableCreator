import pandas as pd
import numpy as np

excelFile = "CS Time Table & List of Courses (Fall 2019) V 2.0.xlsx"
csv1= "TimeTable1.csv"
csv2 = "TimeTable2.csv"
timetable = pd.read_csv(csv1)
row1 = timetable.head()


print(row1.type())