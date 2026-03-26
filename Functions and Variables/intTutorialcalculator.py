#int - Integer 
"""
x = input("what is x? ")
y = input("what is y? ")

z = int(x) + int(y) 

print(z)
"""

#reason we're using int() is because with int(), the code will be 
#concatinated to be the string of what number the use typed e.g 2+1 = 21 with int() it will be 3



"""
We can shorten the code to this below and print direct
"""
#x = int(input("what is x? "))
#y = int(input("what is y? "))
#print(x + y)


#FLOAT - number with decimal point (with this we can accept decimal number with int, it will not work)
x = float(input("what is x? "))
y = float(input("what is y? "))

z = round(x + y)
#print(z)
print(f"{z:,}") #this is use to add comma to digit e.g 1,000,000

#print(round(x + y)) it can be done this way for shorter version 

#to round the number to the nearest figure 

x = float(input("what is x? "))
y = float(input("what is y? "))

z = round(x / y, 2) #this will only give you two decimal number e.g instead of 0.66666666 it will be 0.67
print(f"{z:.2f}") #this will still give you 0.67, instead adding it to z, you can add the it to the print instaed 