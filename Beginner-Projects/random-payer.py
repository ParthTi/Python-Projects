import random as rd
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

Len_names = len(names)
random_name = rd.randint(0, Len_names -1)
person_who_pays = names[random_name]
print("Person who will pay: " + person_who_pays)
