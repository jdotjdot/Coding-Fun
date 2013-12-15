##Google Code Jam 2010 Practice
##Round 1A 2010 'Rotate'
import re

def diagonals(newboard):
    X=len(newboard)
    holder=[]
    #for upper-left to bottom-right:
    for y in range(X): #along y axis
        x=0
        this=''
        while x<X and y<X:
            this+=newboard[y][x]
            x+=1
            y+=1
        holder.append(this)
    for x in range(1,X): #now along x axis
        y=0
        this=''
        while x<X and y<X:
            this+=newboard[y][x]
            x+=1
            y+=1
        holder.append(this)
    return holder

filename=r'C:\Documents and Settings\Me\My Documents\Coding Fun\Google Code Jam\in.txt'
with open(filename,'r') as it:
    temp=it.readlines()

numcases=int(temp.pop(0))

pt=0
notonlydots=re.compile(r'[^\.]{1}')
case=['']*numcases
#Note:
#Can easily rotate whole thing by doing zip(*original[::-1])

for i in range(numcases):
    firstline=temp[pt].strip('\n').split(' ')
    N=int(firstline[0])
    K=int(firstline[1])
    Blue=False
    BlueSearch=re.compile(r'B{'+str(K)+r'}')
    Red=False
    RedSearch=re.compile(r'R{'+str(K)+r'}')
    newboard=[]
    pt+=1
    for ii in range(N):
        #Dump to right--don't bother rotating
        newline=re.sub('0','.',''.join(notonlydots.findall(temp[pt].strip('\n'))).zfill(N))
        newboard.append(newline)
        #Check if any horizontal Join-K's
        if BlueSearch.search(newline):
            Blue=True
        if RedSearch.search(newline):
            Red=True
        pt+=1
    #To save computing time, if both wins already found, end here:
    if Red and Blue:
        case[i]='Both'
        continue
    #Otherwise, go by col and try again:
    cols=zip(*newboard)
    cols=[''.join(k) for k in list(cols)]
    for newline in cols:
        if BlueSearch.search(newline):
            Blue=True
        if RedSearch.search(newline):
            Red=True
    #Again to save computing time if possible
    if Red and Blue:
        case[i]='Both'
        continue
    #Now to make similar diagonal strips:
    #first reverse the newboard, then run diagonal find function on both
    backwardsboard=[a[::-1] for a in newboard]
    diags=diagonals(newboard)+diagonals(backwardsboard)
    for newline in diags:
        if BlueSearch.search(newline):
            Blue=True
        if RedSearch.search(newline):
            Red=True

    #Finally checked everything!
    if Red and Blue:
        case[i]='Both'
    elif Red and not Blue:
        case[i]='Red'
    elif Blue and not Red:
        case[i]='Blue'
    elif not Blue and not Red:
        case[i]='Neither'

with open(r'C:\Documents and Settings\Me\My Documents\Coding Fun\Google Code Jam\out.txt','w') as outputfile:
    outputfile.write('\n'.join(['Case #'+str(num+1)+': '+out for num,out in enumerate(case)]))
