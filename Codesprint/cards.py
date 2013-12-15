####
# Codesprint
# Challenge: Picking Cards
####

import math, sys

####INPUT

#find T
T = raw_input()
T = int(T)

cards = []
for counter in range(T):
    skip = raw_input()
    cards.append(raw_input())

for index, content in enumerate(cards):
    temp = content.split(' ')
    while '' in temp:
        temp.remove('')
    cards[index] = map(int,temp)

##T = 3
##cards = [
##    [0,0,0],
##    [0,0,1],
##    [0,3,3],
##    [4,6,8,7,6,2,2,3,6],
##    [0,0,0,0,0,0,0,0,0,0,5],
##    [2],
##    [0,0,0,1,1,6],
##    [1,2,3,4,5],
##    [0,1,2,3,4,5,6,7]
##    ]

#####CALCULATE

def setup(cards):
    theset = {}
    for k in cards:
        try:
            theset[k] += 1
        except KeyError:
            theset[k] = 1
    return theset

def calculate(cards):
    k = 0
    
    try:
        _cards = cards[k]
    except KeyError:
        return 0
        
    total = _cards
    _cards -= 1
    
    while not (_cards == 0 and k + 1 not in cards.keys()):

        k+=1

        try:
            _cards += cards[k]
        except KeyError:
            pass
            
        total *= _cards
        _cards -= 1
        total %= 1000000007

    else:
        if k < max(cards.keys()):
            return 0
        else:
            return total
        
answers = []
for thisset in cards:
    thisset = setup(thisset)
    answers.append(str(calculate(thisset)))

sys.stdout.write('\n'.join(answers))
