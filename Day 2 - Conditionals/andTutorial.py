'''
This shows how to use "and" 
'''

score = int(input("score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >=80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: c")
elif score >= 60 and score < 70:
    print("Grade: D")
elif score >= 50 and  score < 60:
    print("Grade: E")
else:
    print("Grade: F")

'''
More advanced way to tighten this code up and increase the readability
But i prefer the first one 
'''
if 90 <= score <= 100:
    print("Grade: A")

elif <=80 score < 90:
    print("Grade: B")

elif <= 70 score < 80:
    print("Grade: c")

elif <= 60 score < 70:
    print("Grade: D")

elif <= 50 score < 60:
    print("Grade: E")

else:
    print("Grade: F")