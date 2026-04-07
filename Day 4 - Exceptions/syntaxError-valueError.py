x = int(input("what is x? "))
print(f"x is {x}")

#with any type of number, the code above will work fine 
#but when you string like "cat", that will bring an error called value error 
#ValueError: Invalid literal for int() with base 10: 'cat'


#VALUEERROR 
'''
To catch any type of error, python has a keyword called 'try' 
and check if some has happen, 'except'soome has happen, do this 
- try and except
'''

try:
    x = int(input("what is x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an interger")

#Better pratice - nameError 
'''
Trying to improve the code, so we move the print in try outside both the try and except block 
now we have now encounter a new error called nameError 
Now to solve this error, there is another keyword python support called 'else'
'''
try:
    x = int(input("what is x? "))
except ValueError:
    print("x is not an interger")
else:
    print(f"x is {x}")

'''
To prompt the user to again and again till they put a int
'''
while True: #keep looping till the loop is false 
    try:
        x = int(input("what is x? ")) 
    except ValueError:
        print("x is not an interger") #try block 40, if it is int, skip 41 and 42 and break out of the loop and print the value 
    else:
        break
    #it will keep asking the user "what is x" until they input int and break of the loop 
print(f"x is {x}")


#to make this code shorter, we can break the break forward 
while True: 
    try:
        x = int(input("what is x? ")) 
        break #With this, it immediately check the correctness of "x" and if it's an int, it will break else, it will ask again 
    except ValueError:
        print("x is not an interger") 

print(f"x is {x}")


#creating my function 
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True: 
        try:
            x = int(input("what is x? ")) 
            break
        except ValueError:
            print("x is not an interger") 
    return x

main()

'''
Instead of keeping telliing the user "X is not an interger"
we can use another keyword called 'pass'
'''
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True: 
        try:
            x = int(input("what is x? ")) 
            break
        except ValueError:
            pass #instead of passing the error message, it will just pass and let the loop reprompt the question
    return x

main()

'''
To make it more reuseable, making small changes 
'''

def main():
    x = get_int("what is x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True: 
        try:
            x = int(input(prompt)) 
            break
        except ValueError:
            pass #instead of passing the error message, it will just pass and let the loop reprompt the question
    return x

main()


#RAISE is use to raise keywords - but in next class 
