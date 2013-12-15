filename=r'C:\Documents and Settings\Me\My Documents\Downloads\C-large-practice.in'
with open(filename,'r') as it:
    temp=it.readlines()

temp=list(map(lambda s: s.strip('\n'),temp))
numcases=temp.pop(0)
numcases=int(numcases)

letters=' abcdefghijklmnopqrstuvwxyz'
nums=[0,2,22,222,3,33,333,4,44,444,5,55,555,6,66,666,7,77,777,7777,8,88,888,9,99,999,9999]

def comb(a,b):
    return [a,b]

thedict=dict(list(map(comb,letters,nums)))

output=open(r'C:\Documents and Settings\Me\My Documents\Coding Fun\3-2.txt','w')
a=1
for k in temp:
    holder='q'
    for g in k:
        input2=str(thedict[g])
        if holder[-1]==input2[0]:
            holder+=' '+input2
        else:
            holder+=input2
    holder=holder[1:]
    output.write('Case #' + str(a) +': ' + holder + '\n')
    a+=1

output.close()    
        
