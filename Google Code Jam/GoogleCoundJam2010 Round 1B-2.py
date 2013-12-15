from operator import itemgetter

filename=r'C:\Documents and Settings\Me\My Documents\Coding Fun\Google Code Jam\in.txt'
with open(filename,'r') as it:
    temp=it.readlines()

numcases=int(temp.pop(0))    

pt=0
answers=[]
for line in range(numcases):
    first=temp[pt].split(' ')
    N=int(first[0])
    K=int(first[1])
    B=int(first[2])
    T=int(first[3])
    pt+=1
    X=temp[pt].split(' ')
    pt+=1
    V=temp[pt].split(' ')
    pt+=1
    pair=[dict(num=i,X=int(X[i]),V=int(V[i])) for i in range(N)]
    
    ###Check if possible
    if not sum([1 for num in range(len(pair)) if pair[num]['V']*T+pair[num]['X']>=B])>=K:
        answers.append('IMPOSSIBLE')
        continue

    finished=0
    tester=pair

## Here, was planning to literally run the race and have the chicks
## Move up one by one, but this might be a bad idea in retrospect

##    tester.sort(key=itemgetter('X'))
##    while finished<K:
##        for chick in tester:
##            if chick[
##                chick['X']+=chick['V']
##            if chick['X']>=B:
##                finished+=1
##                tester.remove(chick)
            
