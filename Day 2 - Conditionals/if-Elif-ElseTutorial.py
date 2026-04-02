        x = int(input("what is x? "))
        y = int(input("what is y? "))

        if x < y:
            print("x is less than y")
        if x > y:
            print("x is greater than y")
        if x == y:
            print("x is equal to y")

'''
To improve this, we introduce the word "elif" and "else"
to reduce the repetiton of if and to stop the code, when we have gotten true 
'''

        x = int(input("what is x? "))
        y = int(input("what is y? "))

        if x < y:
            print("x is less than y")
        elif x > y:
            print("x is greater than y")
        else x == y: #we don't have to ask the last question, if x is not greater than y and y is not greater than x, then it must be equal to each other 
            print("x is equal to y")

'''
I want to touch some of the stuff the lecturer talked about "==" and "!="
a little example below 
'''
        x = int(input("what is x? "))
        y = int(input("what is y? "))

        if x == y:
            print("x is equal to y")
        else:
            print("x is not equal to y")

'''
To use the other one "!="
'''
        x = int(input("what is x? "))
        y = int(input("what is y? "))

        if x == y:
            print("x is not equal to y")
        else:
            print("x is equal to y")