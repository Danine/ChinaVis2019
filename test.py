import pandas
import pickle

# day1 = pandas.read_csv('传感器日志数据\day1.csv')

# position = pandas.read_csv('传感器布置表.csv')

# final_day1 = pandas.merge(day1, position, how='left')

# groupbyuser = final_day1.groupby("id")
first_floor = [
    "##############################",
    "##########FF.................#",
    "#AAAAA......###SSSSMMMMMMMMMM#",
    "#AAAAA.PP...###SSSSMMMMMMMMMM#",
    "#BBBBB.PP.TT###SSSSMMMMMMMMMM#",
    "#BBBBB.PP.TT###SSSSMMMMMMMMMM#",
    "#CCCCC.PP.11###SSSSMMMMMMMMMM#",
    "#CCCCC.PP.11###SSSSMMMMMMMMMM#",
    "#DDDDD.PP.11###SSSSMMMMMMMMMM#",
    "#DDDDD.PP.11###SSSSMMMMMMMMMM#",
    "######....22###SSSSMMMMMMMMMM#",
    "######....22###SSSSMMMMMMMMMM#",
    "#.QQQQ.......................#",
    "I.QQQQ.......................#",
    "#.........ff.......HH333344tt#",
    "##I#IO#I#######O#O#HH333344tt#"
]
def read_walk():
    with open("user_walk.pkl", 'rb') as fp: 
        return pickle.load(fp)

if __name__ == "__main__":
    user_walk = read_walk()
    for single_user, single_walk in user_walk.items():
        print(single_walk)
        input()
    print(1)