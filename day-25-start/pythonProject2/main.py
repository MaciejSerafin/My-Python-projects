# # with open("./weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open('weather_data.csv') as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # # print(temp_list)
# #
# # # sum = 0
# # # for temp in temp_list:
# # #     sum += temp
# # #
# # # print(sum)
# # # print(sum/len(temp_list))
# #
# # # average = sum(temp_list) / len(temp_list)
# # # print(average)
# #
# # print(data["temp"].mean())
# #
# # # print(max(temp_list))
# #
# # print(data["temp"].max())
#
#
# # print(data[data.day == "Monday"])
#
# # print(data[data.temp == data.temp.max()])
# #
# # monday = data[data.day == "Monday"]
# # print(monday.condition)
# # print(monday)
# #
# # monday = data[data.day == "Monday"]
# # monday_temp = monday.temp[0]
# # far = monday_temp * 2 + 30
# # print(far)
#
# #Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
#
# data.to_csv("new_data.csv")

#Squirell counter

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240313.csv")

data_dict = {
    "color": ["grey", "cinamon", "black"],
    "count": []
}

gray = len((data[data["Primary Fur Color"]  == "Gray"]))
print(gray)

cinnamon = len((data[data["Primary Fur Color"]  == "Cinnamon"]))
print(cinnamon)

black = len((data[data["Primary Fur Color"]  == "Black"]))
print(black)

data_dict["count"].append(gray)
data_dict["count"].append(cinnamon)
data_dict["count"].append(black)

print(data_dict)

data = pandas.DataFrame(data_dict)

data.to_csv("new_data.csv")



