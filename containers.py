print("EX. 1 Answer: ")
students = ['steve','jeff','mindy','susan','fred','george']

print(students[1])
print(students[-1])
# -------------------------------------------
print("EX. 2 Answer: ")
foods = ('hot and spicy snail sauce noodles','guamanian spared-ribs','hong shao rou','pork mac and cheese','hot-pot','shabu-shabu')
for f in foods:
    print(f"{f} is a good food")

# -------------------------------------------
print("EX. 3 Answer: ")
for f in foods[-2:]:
    print(f)
# -------------------------------------------
print("EX. 4 Answer: ")
home_town = {
    'city': 'Biddeford',
    'state': 'ME',
    'population': 21000,
}
print(f"I was born in {home_town['city']}, {home_town['state']}.  With a whoppingly huge population of {home_town['population']} people.")

# -------------------------------------------
print("EX. 5 Answer: ")
for i, j in home_town.items():
    print(f"{i} = {j}")

# -------------------------------------------
print("EX. 6 Answer: ")
cohort = []
for i, student in enumerate(students):
    cohort.append({
        'student': student,
        'fav_food': foods[i]})
    print(cohort[i])

# -------------------------------------------
print("EX. 7 Answer: ")
awesome_students = [(f"It's possible that {s} is awesome!") for s in students[:-1]]
for s in awesome_students:
    print(s)
print(f"It's possible that.... no... Sorry {students[-1]}, just not feeling the awesome vibes from ya...")
print(awesome_students)
# -------------------------------------------
print("EX. 8 Answer: ")
a_foods = [f for f in foods if 'a' in f]
for f in a_foods:
    print(f)
# -------------------------------------------