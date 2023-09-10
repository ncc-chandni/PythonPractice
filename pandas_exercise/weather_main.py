import csv

with open("/Users/umakantmanore/Desktop/amu/practice/pandas_exercise/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        # print(row)
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)

import pandas as pd
import math

data = pd.read_csv("/Users/umakantmanore/Desktop/amu/practice/pandas_exercise/weather_data.csv")
print(data)

temp_list = data["temp"].to_list()
avg = sum(temp_list)/len(temp_list)
print(avg)
avg = data["temp"].mean()
print(avg)

print(data.day[data.temp == data.temp.max()])