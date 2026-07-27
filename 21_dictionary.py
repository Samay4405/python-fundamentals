# dictionary = a collection of {key: value} pairs ordered and changeable. No duplicates


capitals = {"USA": "Washington D.C.", 
            "UK": "London",
            "India": "New Delhi",
            "China": "Beijing"}

# print(capitals.get('USA'))                               # It will print the capital
# print(capitals.get('Japan'))                             # It will print the None if its not in the list
# capitals.update({"USA":"Detriot"})                       # It will update the capital
# capitals.update({"Germany": "Berlin"})                   # It will add in the list

# capitals.pop("UK")                                       # It will remove the country
# capitals.popitem()                                       # It will remove the latest country
# print(capitals)
# capitals.clear()                                         # It will clear the entire list.


# keys = capitals.keys()                                            # It will only print the enitre countrys but not the capital.

# for keys in capitals.keys():
 
#     print(keys)

# values = capitals.values()                                 # It will only print the capital.
# for values in capitals.values() :

#     print(values)
    
items = capitals.items()                                   # Items return a dictionay object which resembles a 2d-list of tuples.
for key, value in capitals.items():                        # It will print the country and capital.
    print(f"{key} : {value}")
