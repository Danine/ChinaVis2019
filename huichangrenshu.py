import pandas as pd
import copy
import pickle

day = pd.read_csv('map_min\day03.csv')
day = day.sort_values(by=['time','floor'], ascending=True)
print(day)

first_floor = [
    "###############################",
    "####################O##########",
    "###########FF.................#",
    "##AAAAA......###SSSSMMMMMMMMMM#",
    "##AAAAA.PP...###SSSSMMMMMMMMMM#",
    "##BBBBB.PP.TT###SSSSMMMMMMMMMM#",
    "##BBBBB.PP.TT###SSSSMMMMMMMMMM#",
    "##CCCCC.PP.11###SSSSMMMMMMMMMM#",
    "##CCCCC.PP.11###SSSSMMMMMMMMMM#",
    "##DDDDD.PP.11###SSSSMMMMMMMMMM#",
    "##DDDDD.PP.11###SSSSMMMMMMMMMM#",
    "#######....22###SSSSMMMMMMMMMM#",
    "#######....22###SSSSMMMMMMMMMM#",
    "##.QQQQ.......................#",
    "#I.QQQQ.......................#",
    "##.........ff.......HH333344tt#",
    "###I#IO#I#######O#O#HH333344tt#"
]
second_floor = [
    "###############################",
    "###############################",
    "###########FF##################",
    "##RRRRR......##################",
    "##RRRRR......##################",
    "##RRRRR....TT##################",
    "##RRRRR....TT##################",
    "##RRRRR....66##################",
    "##RRRRR....66##################",
    "##RRRRR....####################",
    "##RRRRR....####################",
    "##55555....####################",
    "##55555....####################",
    "#######......##################",
    "#EEEEEE......##################",
    "#EEEEEE....ff##################",
    "#EEEEEE########################"
]
# A = {}; B = {}; C = {}; D = {}; Q = {}; P = {}; T1 = {}; T2 = {}; 
# R1 = {}; R2 = {}; R3 = {}; R4 = {}; S = {}; M = {}; H = {}; 
# R = {}; R5 = {}; R6 = {}; E = {}; T3 = {}; 

data = {'first_floor':{}, 'second_floor':{}}

for i in range(len(day.nop)):
    if day.floor[i] == 1:
        floor = data['first_floor']
        label = first_floor[day.x[i]][day.y[i]]
    else:
        floor = data['second_floor']
        label = second_floor[day.x[i]][day.y[i]]
    if label not in floor:
        floor[label] = {}
    floor[label][day.time[i]] = day.nop[i] + floor[label].get(day.time[i],0)

data_output = open('map_min/day3.pkl','wb')
pickle.dump(data, data_output)
data_output.close()

print(0)

# for i in range(len(day.nop)):
#     if day.floor[i] == 1 and first_floor[day.x[i]][day.y[i]] == 'A':
#         if day.time[i] in A:
#             A[day.time[i]] += day.nop[i]
#         else:
#             A[day.time[i]] = day.nop[i]
#     elif day.floor[i] == 1 and first_floor[day.x[i]][day.y[i]] == 'B':
#         if day.time[i] in B:
#             B[day.time[i]] += day.nop[i]
#         else:
#             B[day.time[i]] = day.nop[i]
#     elif day.floor[i] == 1 and first_floor[day.x[i]][day.y[i]] == 'C':
#         if day.time[i] in C:
#             C[day.time[i]] += day.nop[i]
#         else:
#             C[day.time[i]] = day.nop[i]
#     elif day.floor[i] == 1 and first_floor[day.x[i]][day.y[i]] == 'D':
#         if day.time[i] in D:
#             D[day.time[i]] += day.nop[i]
#         else:
#             D[day.time[i]] = day.nop[i]
#     elif day.floor[i] == 1 and first_floor[day.x[i]][day.y[i]] == 'Q':
#         if day.time[i] in Q:
#             Q[day.time[i]] += day.nop[i]
#         else:
#             Q[day.time[i]] = day.nop[i]
#     elif day.floor[i] == 1 and first_floor[day.x[i]][day.y[i]] == 'P':
#         if day.time[i] in P:
#             P[day.time[i]] += day.nop[i]
#         else:
#             P[day.time[i]] = day.nop[i]
    