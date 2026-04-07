students = ["Joahua", "David", "Marvellous"]

for student in students:
    print(student)

'''
There is a longer way of writing it, if you want to pick only one name 

students = ["Joshua", "David", "Marvellous"]
print(student[0])
print(student[1])
print(student[2])

''''
'''
if you're working with big database that has more that 100 list 
we can use the code below 


students = ["Joshua", "David", "Marvellous"]

for i in range(len(students)):
    print(i + 1, students[i])   
       

this code above literally show numbers to each of the list 
adding 1 to the i, make it stop counting from 0, it will start from 1
now with this, you can know each number of the data in the list 