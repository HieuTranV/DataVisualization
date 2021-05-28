# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 02:33:19 2015

@author: nymph
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

############################## Your code for loading and preprocess the data ##
file_path = "./household_power_consumption.txt"
all_data = pd.read_csv(file_path, delimiter=";", low_memory=False)
print(all_data)

data = all_data.loc[(all_data.Date == '2/2/2007') | (all_data.Date == '1/2/2007')]
data["Datetime"] = pd.to_datetime(data["Date"]+ " "+ data["Time"])
data.drop(["Date", "Time"], axis = 1, inplace=True)
numeric_features = list(set(data.columns) - set(["Datetime"]))
data[numeric_features]=data[numeric_features].apply(lambda x:pd.to_numeric(x, downcast='float', errors='ignore'))

def count_specical_value(Sr, key="?"):
    dict_values = Sr.value_counts()
    if key in dict_values.keys():
        return dict_values[key]
    return 0

print(data.agg(count_specical_value))


data.Datetime = data.Datetime.map(lambda x:x.ctime())
data.set_index("Datetime", inplace=True)


############################ Complete the following 4 functions ###############
def plot1():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    bins = np.arange(0, max(data["Global_active_power"]), 0.5)
    ax.hist(data["Global_active_power"], color='red', edgecolor='black', bins=bins)
    plt.xticks(list(range(0, int(max(data["Global_active_power"])), 2)))
    plt.ylabel("Frequency")
    plt.xlabel("Global Active Power (kilowatts)")
    plt.title("Global Active Power")
    fig.savefig('./plot1.png', bbox_inches='tight')
    plt.show()
    pass

def plot2():
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.plot(data["Global_active_power"], color='black')
    ticks = ["Thu", "Fri", "Sat"]
    yticks = list(range(0, int(max(data["Global_active_power"])), 2))
    plt.xticks([0, data.shape[0] / 2, data.shape[0]], ticks)
    plt.yticks(yticks)
    plt.ylabel("Global Active Power (kilowatts)")
    fig.savefig('./plot2.png', bbox_inches='tight')
    plt.show()
    pass

def plot3():
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.plot(data["Sub_metering_1"], color='black')
    ax.plot(data["Sub_metering_2"], color='red')
    ax.plot(data["Sub_metering_3"], color='blue')
    ax.legend(["Sub_metering_1", "Sub_metering_2", "Sub_metering_3"])
    ticks = ["Thu", "Fri", "Sat"]
    yticks = list(range(0, int((max(data["Sub_metering_1"]))), 10))
    plt.yticks(yticks)
    plt.xticks([0, data.shape[0] / 2, data.shape[0]], ticks)
    plt.ylabel("Energy sub metering")
    fig.savefig('./plot3.png', bbox_inches='tight')
    plt.show()
    pass

def plot4():
    fig = plt.figure(figsize=(15, 10))

    ax1 = fig.add_subplot(221)
    ax1.plot(data["Global_active_power"], color='black')
    ticks = ["Thu", "Fri", "Sat"]
    plt.xticks([0, data.shape[0] / 2, data.shape[0]], ticks)
    plt.yticks(list(range(0, int(max(data["Global_active_power"])), 2)))
    plt.ylabel("Global Active Power")

    ax2 = fig.add_subplot(222)
    ax2.plot(data["Voltage"], color='black')
    yticks = list(range(int(data["Voltage"].min() + 1), int(data["Voltage"].max() + 1), 4))
    ticks = ["Thu", "Fri", "Sat"]
    plt.xticks([0, data.shape[0] / 2, data.shape[0]], ticks)
    plt.yticks(yticks)
    plt.xlabel("datetime")
    plt.ylabel("Voltage")

    ax3 = fig.add_subplot(223)
    ax3.plot(data["Sub_metering_1"], color='black')
    ax3.plot(data["Sub_metering_2"], color='red')
    ax3.plot(data["Sub_metering_3"], color='blue')
    ax3.legend(["Sub_metering_1", "Sub_metering_2", "Sub_metering_3"])
    yticks = list(range(0, int((max(data["Sub_metering_1"]))), 10))
    ticks = ["Thu", "Fri", "Sat"]
    plt.yticks(yticks)
    plt.xticks([0, data.shape[0] / 2, data.shape[0]], ticks)
    plt.ylabel("Energy sub metering")

    ax4 = fig.add_subplot(224)
    ax4.plot(data["Global_reactive_power"], color='black')
    ticks = ["Thu", "Fri", "Sat"]
    plt.xticks([0, data.shape[0] / 2, data.shape[0]], ticks)
    plt.ylabel("Global Rective Power")
    plt.xlabel("datetime")
    fig.savefig('plot4.png', bbox_inches='tight')
    plt.show()
    pass

plot1()
plot2()
plot3()
plot4()

