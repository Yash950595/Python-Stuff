#Nested lists in dictonary

'''
travel_log={
    "Singapore": ["Queensland","Sentosa Island", "Jurong Gateway"],
    "Mumbai": ["Thane","Nerul","VT","Malabar Hills"],
}

print(travel_log["Singapore"][2]) #Singapore is the key and 2 is the index number of element in the list

#nested list

new_list=["A","B",["C","D"]]

print(new_list[2][1])
'''
'''
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}

print(travel_log["Germany"]["total_visits"])
'''

starting_dictionary = {
    "a": 9,
    "b": 8,
}

starting_dictionary["c"]=7
final_dictionary=starting_dictionary
print(final_dictionary)

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
for key in dict:
    v=dict[key]=+1
print(v)