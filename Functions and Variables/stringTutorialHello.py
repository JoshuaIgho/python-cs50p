#STRINGS - str

#Ask the user of their name 
name = input("What is your name? ").title().strip()

#title() helps to capitalize the text (e.g joshua igho efe = Joshua Igho Efe)
#capitalize() only capitalize the first text
#strip() remove whitespaces from the text before and after but not inbetween 

#name = name.title()
#name = name.strip().  we can break it down like this because if we keep adding the method, the code might look like a mess

#Split user's name into first and last name (if you want only one part of the name)
first, last = name.split(" ")

#Say hello to the user 
print("Hello,", first)

#you can use different way to concantinate code 
#1 print("Hello, " + name)
#2 print("Hello,", name)

