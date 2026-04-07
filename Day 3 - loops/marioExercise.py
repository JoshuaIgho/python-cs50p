def main():
    n = int(input("n? "))
    printColum(n)
    

def printColum(height):
    print("#\n" * height, end="")

main()




def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()