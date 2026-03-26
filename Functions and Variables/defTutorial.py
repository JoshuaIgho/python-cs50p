'''
1. def means define, we define a function that donot exist in python 
'''

def hello(): #when defining a function, the definition go below the code and some step to the right 
    print("hello") #anytime function hello() is called, it will print hello 


name = input("what is your name? ")
hello()
print(name)


'''
2. To make the code more advance, we will not just call the hello() but it will take a parameter 
'''

def hello(to="world"): #it takes a para and a default name, incase the programmer didn't put name, it will falls to hello word 
    print("hello,", to) #this will extract the text from the to or fall back to default "world"


hello() #since the programmer has not input anything at this time, it will be "hello world"
name = input("what is your name? ") #Whatever the user typed in, will be saved to name
hello(name) #name is the argument been passed === hello(what the user typed)


'''
3. We went more deeper here, this way, we can put the function of hello() way down and it will still work 
'''
def main():
    name = input("what is your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()