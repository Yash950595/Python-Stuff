'''
with open("CSV and pandas\weather_data .csv") as data:
    p=data.readlines()
    print(p)
'''

'''
import csv
with open("CSV and pandas\weather_data .csv") as data_file:
    data=csv.reader(data_file)
    temperatures=[]
    for row in data: #We got an eror over here because we trying to loop the data_file instead of data
                     #Compiler misinterpreted and printed second letter of the first word thinking it as index no.1
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
   
'''
'''
# To avoid such complex method or way we use PANDAS which are beneficial for handling big data
import pandas
data=pandas.read_csv("CSV and pandas\weather_data .csv")
print(data["temp"])

print(data["temp"].mean())

print(data["temp"].max())
'''

import pandas

data = pandas.read_csv("CSV and pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count=len(data[data["Primary Fur Color"]=="Gray"])
cinnamon_squirrels_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels_count=len(data[data["Primary Fur Color"]=="Black"])
print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

dict={
    "Fur Color":["Gray","Red","Black"],
    "Count":[grey_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}

df=pandas.DataFrame(dict)
df.to_csv("CSV and Pandas/Final_count.csv") #here we had error as we only wrote the csv file name and 
                                            #not the relative address

                                            