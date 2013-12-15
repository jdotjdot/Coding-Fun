####
# Codesprint
# Challenge: Permutation
# First submissions to Codesprint, testing
#   so uploading, stdin errors expected for first
#   few tries
####

import sys
import itertools as it

####INPUT

# find n
n = raw_input()

V=[]
for counter in range(int(n)):
    V.append(raw_input())

for index, content in enumerate(V):
    forV = content.split(' ')
    while '' in forV:
        forV.remove('')
    V[index] = map(int,forV)

##n=3
##V=[[0,4,5],[2,0,-2],[0,0,0]]

####CALCULATION

perms = it.permutations(range(int(n)))

best = {'Permutation': None, 'Score':0}

while True:
    try:
        current = perms.next()
    except StopIteration:
        break

    #consecs: [ [1,2] , [2,3] , [3,4] ] etc.
    consecs = [current[k:k+2] for k in range(len(current)-1)]

    score = sum(map(lambda s: V[s[0]][s[1]],consecs))
    if score > best['Score']:
        best['Score'] = score
        best['Permutation'] = current

sys.stdout.write(
            ' '.join([str(k) for k in best['Permutation']])
            )
        
