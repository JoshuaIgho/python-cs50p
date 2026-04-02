name = input("what is your name? ")

match name:
    case "Henry" | "Joshua" | "Ron":
        print("Lagos")
    case "Desmond" :
        print("Ikeja")
    case _ : #when the inputed is not hard coded 
        print("who")

    