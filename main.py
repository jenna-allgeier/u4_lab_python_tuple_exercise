# # exercise 1 -------------------------------
students = ["Sam", "Mark", "Ife"]
# last_index = len(students) - 1
# print(students[1])
# print(students[last_index])

# # exercise 2 -------------------------------
food_tup = ("spaghetti", "broccoli", "fish")
# for food in food_tup:
#     print(food, ' is a good food.')

# # exercise 3 -------------------------------

# for x in range(-1,-3,-1):
#     print(f'{food_tup[x]} is a good food.')

# for index, value in enumerate(food_tup):
#     if (food_tup.len(food_tup)):
#     print(f'{value[index]} is a good food')

# # exercise 4 -------------------------------
# home_town = {
#     "city": "Auburn",
#     "state": "California",
#     "population": 14011
# }
# # print("I was born in", home_town["city"],",",home_town["state"], "~ population of", home_town["population"])

# # exercise 5 -------------------------------
# for key in home_town:
#     print(f'{key} = {home_town[key]}')

# exercise 6 -------------------------------
# cohort = []

# for i, student in enumerate(students):
#     cohort.append({"student": student, "fav_food": food_tup[i]})

# print(cohort)

# exercise 7 -------------------------------
# awesome_students = [(x + " is awesome!") for x in students]

# print(awesome_students)

# exercise 8 -------------------------------
output = [x for x in food_tup if 'a' in x]

for food in output:
    print(food)

   
