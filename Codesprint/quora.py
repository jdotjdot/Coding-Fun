######
# Codesprint
# Challenge: Quora
######

### Real input
first = raw_input()
first = first.split(' ')
T = int(first[0])
Q = int(first[1])
N = int(first[2])

topics = {}
for a in range(T):
    temp = raw_input()
    temp = temp.split(' ')
    topics[int(temp[0])] = (float(temp[1]), float(temp[2]))

questions = {}
for a in range(Q):
    temp = raw_input()
    temp = temp.split(' ')
    if int(temp[1]) > 0:
        questions[int[temp[0]]] = map(int,temp[2:])
    else: 
        questions[int[temp[0]]] = None
