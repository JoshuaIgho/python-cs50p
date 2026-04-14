'''
python comes with a random library
we use Import in python to import some module in python
'''


'''
this can be use when importing a lot of module 
so to keep the code readable
'''
import random #this inmport all the random

coin = random.choice(["heads", "tails"])
print(coin)


"If we are importing just one module, this is a good way"
from random import choice 

coin = choice(["heads", "tails"])
print(coin)

'''
Another random module 
'''

import random

number = random.randint(1, 10) #this will give you number randomly from 1 to 10
print(number )

'''Another random'''
import random
cards = ["jack", "queen", "king"]
random.shuffle(cards) 
print(cards) #this will print just everything in card
for card in cards:
    print(card) #this will print them one after the other and also shuffle them 


