
students = {
    "Joshua": "Lagos",
    "Alex": "London",
    "Favour": "Thailand",
    "David": "Australia"
}
 
print(students["Joshua"])
print(students["Alex"])
print(students["Favour"])
print(students["David"])


#with the code above, what understand is the student is the dict or like a database 
# anytime we can each student name, it will give us the details the student is carryig 

for student in students:
    print(student, students[student], sep=", ")

#we can also print this way, by using loop 
#the first student, will only print out the name and the second will print the location or the details it carries
# and the sep, gives a comma between the name and the location

students = [
    {"name": "Joshua", "house": "Lagos", "patronus": "Otter"},
    {"name": "Alex", "house": "London", "patronus": "stag"},
    {"name": "Favour", "house": "Thailand", "patronus": "Jack Russell terrier"},
    {"name": "David", "house": "Australia", "patronus": None}, #david didn't have patronous and there is function called None, that's why we use None
]
 
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")