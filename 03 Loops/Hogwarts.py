################ LISTS ################
# Example 1
'''students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])'''


# Example 2
'''students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)'''


# Example 3
'''students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])'''



################ DICTIONARIES ################
# Example 1 (not great)
'''students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]'''


# Example 2 (looks bad)
'''students = {"Hermione":"Gryffindor", "Harry":"Gryffindor", "Ron":"Gryffindor", "Draco":"Slytherin"}

print(students["Hermione])'''


# Example 2.1 (easier to read)
'''students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
    }

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])'''


# Example 2.2
'''students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
    }

for student in students:
    print(student)'''


# Example 2.3
'''students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
    }

for student in students:
    print(student, students[student], sep=", ")'''


# Example 3 (more than one key-value pair in a list, or dictionaries nested in a list)
students = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell Terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus":None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")