# with open("weather_data.csv") as data:
# 	data = data.readlines()
# 	print(data)

# import csv

# with open("weather_data.csv") as data_file:
# 	data = csv.reader(data_file)
# 	temparatures = []
# 	for row in data:
# 		if row[1] != "temp":
# 			temparatures.append(row[1])
# 	print(temparatures)

import pandas

0
data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_dict()
print(temp_list)
# Average temperature in the data set
"""avg = sum(temp_list.values()) / len(temp_list)
print(avg)
"""
# Same result with pandas.Series
"""print(data["temp"].mean())
   print(data["temp"].max())
"""
# Get Data in Columns
"""print(data["condition"])
"""
# Pandas Series
"""print(data.condition)
"""
# Get Data in Row
"""print(data[data.day == "Monday"])
"""
print(data[data.temp == data.temp.max()])
# Create DataFrame
df = pandas.DataFrame(data_dict)
print(df)
