def permutations(iterable, r=None):
    pool=tuple(iterable)
    n=len(pool)
    r=n if r is None else r
    if r>n:
        return
    indices=list(range(n))
    cycles=range(n,n-r,-1)
    

filename=r'C:\Documents and Settings\JJ\My Documents\Downloads\A-small-practice (2).in'
with open(filename,'r') as it:
    temp=it.readlines()
temp=list(map(lambda s: s.strip('\n'),temp))
numcases=temp.pop(0)
numcases=int(numcases)
newit=open(r'C:\Documents and Settings\Me\My Documents\Coding Fun\A-1.txt','w')

line=0
caseno=1
from operator import mul
import itertools
while line < len(temp):
    holder=9^10
    numcoords=int(temp[line])
    line+=1
    v1=temp[line]
    line+=1
    v2=temp[line]
    v1=v1.split(' ')
    v1=list(map(int,v1))
    v2=v2.split(' ')
    v2=list(map(int,v2))

    

##    vv1=list(map(list,itertools.permutations(v1,numcoords)))
##    vv2=list(map(list,itertools.permutations(v2,numcoords)))
##    for i in vv1:
##        abhi=0
##        for j in vv2:
##            abhi=list(map(mul,i,j))
##            abhi=sum(abhi)
##        if abhi<holder: holder=abhi
##        #print('going')
    
    newit.write('Case #' + str(caseno) + ': ' + str(holder) + '\n')
    caseno+=1
    line+=1
    print('yeahhh')

newit.close()
print('Done!')
    #10:44
