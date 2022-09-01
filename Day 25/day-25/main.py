# with open("weather_data.csv", mode="r") as file:
#     data = file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     headings = next(data)
#     for row in data:
#         print(row)
#         temperatures.append(int(row[1]))
#         print(temperatures)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# with Pandas
# print(data["temp"].mean())
# print(data["temp"].max())

# # Get data in columns
# print(data["condition"])
# print(data.condition)

# # Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 1.8 + 32
# print(monday_temp_f)

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Cinnamon", "Gray", "Black"],
    "Count": [cinnamon, gray, black]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel.csv")


print(data_dict)







