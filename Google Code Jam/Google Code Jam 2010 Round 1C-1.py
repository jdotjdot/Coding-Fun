## Google Code Jam Round 1C 2010, practice
## 7/21/2011

## Rope Intranet

from itertools import combinations as C

filename=r'C:\Documents and Settings\Me\My Documents\Coding Fun\Google Code Jam'
with open(filename + r'\in.txt', 'r', encoding='utf8') as it:
    temp=it.readlines()

numcases=int(temp.pop(0).strip('\n'))

pt=0
case=[]
for i in range(numcases):
    intersections=0
    N=int(temp[pt].strip('\n'))
    pt+=1
    wires=[]
    for ii in range(N):
        line=temp[pt].strip('\n').split(' ')
        wires.append([int(line[0]),int(line[1])])
        pt+=1
    #Now that all the data is read in...
    for k in C(wires,2):
        #find difference and multiply
        #if answer is negative, there's an intersection, because
        #A1>A2 and B1<B2 or vice versa.  If positive, then
        #one wire is completely higher than the other.
        #Using timeit.Timer, turns out multiplication is faster
        #than boolean >
        if (k[0][0]-k[1][0])*(k[0][1]-k[1][1]) < 0:
            intersections+=1
    case.append(intersections)

with open(filename + r'\out.txt','w') as outputfile:
    outputfile.write('\n'.join(['Case #'+str(num+1)+': '+str(ans) for num,ans in enumerate(case)]))
