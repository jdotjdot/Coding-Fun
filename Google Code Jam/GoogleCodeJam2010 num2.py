thefile=r'C:\Documents and Settings\Me\My Documents\Downloads\B-large-practice.in'

##read it in
with open(thefile, 'r') as it:
    temp=it.readlines()

temp=list(map(lambda s: s.strip('\n'),temp))
num=temp.pop(0)
num=int(num)

newit=open(r'C:\Documents and Settings\Me\My Documents\Coding Fun\2-2.txt','w')

for k in range(num):
    casenum=k+1
    temp2=temp[k].split(' ')
    temp2.reverse()
    newit.write('Case #' + str(casenum) + ': ' + ' '.join(temp2) +'\n')

newit.close()
