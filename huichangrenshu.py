import pandas as pd
'''
fenhuichangA
'''
day = pd.read_csv('map_min\day01.csv')
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

for i in range(len(day.nop)):
    if day.floor == 1 and 2 < day.x < 5 and 1 < day.y < 7:
        day.nop[i] = (day.nop[i] + 59)// 60
        # print(day.nop[i])
day.to_csv('map_min\day001.csv')