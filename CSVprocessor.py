import pandas as pd

day = pd.read_csv('map_min\day3.csv')

for i in range(len(day.x)):
    day.x[i] += 1
    if day.nop[i] != 0:
        day.nop[i] = (day.nop[i] + 59)// 60
        # print(day.nop[i])
day.to_csv('map_min\day03.csv')