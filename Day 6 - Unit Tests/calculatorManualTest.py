from calculator import square 

def main():
    testCalculator()

def testCalculator():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 is not equal 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 is not equal 9")       

if __name__ == "__main__":
    main()

# To the testing anutomatically 