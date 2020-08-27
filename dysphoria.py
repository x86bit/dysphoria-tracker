from tkinter import *
import matplotlib.pyplot as plt
import re
from datetime import date
valueDict = {1 : ["None!", "#2b9e49"], 2 : ["A tiny bit...", "#62bd1c"], 3 : ["Not enough to ruin the day!", "#8fbd1a"], 4 : ["Not much.", "#adbd1a"], 5 : ["Fifty fifty", "#f0b105"],
6 : ["Quite a bit", "#f07605"], 7 : ["Alot", "#f04705"], 8 : ["Dysphoria all day", "#f02005"], 9 : ["One of the worst days of my life", "#de2f2f"], 10 : ["I want to die", "#e10000"]}
def changeValue(value):
    value = int(value)
    good_bad = Label(main, text = "                                                                 ")
    good_bad.grid(row = 2, column = 0)
    try:
        good_bad = Label(main, text = valueDict[value][0], fg = valueDict[value][1])
        good_bad.grid(row = 2, column = 0)
    except KeyError:
        pass
def recordData():
    value = scale.get()
    file = open("days.txt", "a+")
    file.write("Scale: " + str(value) + " Date: " + str(date.today()) + "\n")
    file.close()
def viewGraph():
    file = open("days.txt", "r+")
    data = file.read().split("\n")[:-1]
    iterate = 0
    for i in range(len(data)):
        match = re.search("Scale: (.+?) Date: ", data[iterate])
        if match:
            found = match.group(1)
            data[iterate] = int(found)
        iterate += 1
    data.insert(0, 0)
    plt.plot(data, marker = "D")
    plt.grid()
    axes = plt.gca()
    axes.set_xlim([0, len(data)-1])
    axes.set_ylim([0, 10])
    plt.xlabel("Days of recording")
    plt.ylabel("Scale of dysphoria")
    plt.show()
main = Tk()
howBad = Label(main, text = " How bad was gender dysphoria today? ")
scale = Scale(main, from_ = 1, to = 10, orient = HORIZONTAL, length = 150, command = changeValue)
good_bad = Label(main, text = valueDict[1][0], fg = valueDict[1][1])
submit = Button(main, text = " Submit ", command = recordData)
graph = Button(main, text = " View Graph ", command = viewGraph)
howBad.grid(row = 0, column = 0)
scale.grid(row = 1, column = 0)
good_bad.grid(row = 2, column = 0)
submit.grid(row = 3, column = 0)
graph.grid(row = 4, column = 0)
main.mainloop()
