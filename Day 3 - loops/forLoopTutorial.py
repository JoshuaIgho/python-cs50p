for i in [0, 1, 2]:
    print("meow")

#incase we have million of numbers 

for i in range(10000000):
    print("meow")

for _ in range(3):  #when you don't need the name
    print("meow")

print("meow\n" * 3, end="") #this is another way to do this but it's not advisable to use 

'''
Trying to collect data from user to know how many time the cat should meow 
'''



while True: #when you want to do something again and again until u get the real answer
    n = int(input("what is n? "))
    if n > 0: #if n is greater than 0, if not 
        break  #then stop asking, countinue asking same question

for _ in range(n):
    print("meow")




#using it as a function
def main():
    number = get_number()
    meow(number)

    def get_number():
        while True:
            n = int(input("what is n? "))
            if n > 0:
                return n

def meow(n):
    for _ in range(n)