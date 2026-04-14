
#value typed into commandline 
#sys.argv - this show what the user has typed before they click enter 

import sys

print("hello, my name is", sys.argv[1]) #write your name before clicking enter


'''In the case the user doesn't type their name '''
import sys

try:
    print("hello, my name is", sys.argv[1]) #write your name before clicking enter
except:
    print("Too few argument")

#OR instead of exceptions 
import sys

if len(sys.argv) < 2 :
    print("Too few arguments")
elif len(sys.argv) > 2 :
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
    
#incase you don't want to use else 
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])

#To get multiple names printed, it will be line by line  
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

