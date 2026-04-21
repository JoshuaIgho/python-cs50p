def main():
    x = int(input("Number to square "))
    print(square(x))


def square(n):
    return n * n

#Why i am not closing the main() is because I'm exporting the file or i can do it this way below

if __name__ == "__main__":
    main()