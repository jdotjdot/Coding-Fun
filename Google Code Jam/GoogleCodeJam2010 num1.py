#Let's get started!
import easygui

def solve(C, I, P):
    P=P.split(" ")
    P=[int(k) for k in P]
    import itertools
    combos=list(itertools.combinations(P,2))
    #sumcombos=list(itertools.starmap(sum,combos))
    sumcombos=[sum(k) for k in combos]
    prices=list(combos[sumcombos.index(int(C))])
    if prices[0]==prices[1]:
        temp=P.index(prices[0])
        P.remove(temp)
        return [str(temp+1), str(P.index(prices[1])+2)]
    else:
        return [str(P.index(prices[0])+1), str(P.index(prices[1])+1)]

#joe=easygui.fileopenbox('get it')
joe=r'C:/Documents and Settings/Me/My Documents/Downloads/A-large-practice.in'
with open(joe, 'r', encoding='utf8') as it:
    temp=it.readlines()

temp=list(map(lambda s: s.strip('\n'),temp))
temp[0]=int(temp[0])
numbercases=temp.pop(0)
for k in range(int(numbercases)):
    answer=solve(temp[3*k],temp[3*k+1],temp[3*k+2])
    print("Case #" + str(k+1) + ": " + ' '.join(answer))
        

        
    
    
