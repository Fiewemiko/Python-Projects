import pandas

# data = pandas.read_csv("226 weather-data.csv")
# type(data)
#
# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
# print(sum(temp_list)/len(temp_list))
# print(data.temp)

# bring column
# print(data.temp)
# #bringh value
# print(data[data.temp == data.temp.max()])
#
#
# tempF = []
# for temp in data.temp:
#     tempFF = temp *9/5 +32
#     tempF.append(tempFF)
#
# print(tempF)

# #Create a dataframe from Scratch
# data_dict = {
#     "Students": ["Amy","James","Angela"],
#     "Scores": [76,56,65]
# }
# students = pandas.DataFrame(data_dict)
# students.to_csv("Students.csv")
# print(students)
#
# data.to_dict()


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur = data["Primary Fur Color"].to_csv()
print(fur)

grey = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])


fur_colors = {'Fur Color': ['grey', 'red', 'black'],
              'Count': [grey, red, black]}

df = pandas.DataFrame(fur_colors)
df.to_csv("squirrel_count")
