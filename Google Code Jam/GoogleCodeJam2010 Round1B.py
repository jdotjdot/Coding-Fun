filename=r'C:\Documents and Settings\Me\My Documents\Coding Fun\Google Code Jam\in.txt'
with open(filename,'r') as it:
    temp=it.readlines()

def DirectoryMaker(MyList, dictionary):
    if len(MyList)==0: return
    if MyList[0] not in dictionary.keys():
        dictionary[MyList[0]]=dict()
    DirectoryMaker(MyList[1:],dictionary[MyList[0]])
    #    dict([['home',dict([['gcj',dict([['finals',dict()]])]])]])

def DirectoryChecker(MyList, dictionary):
    if len(MyList)==0: return 0
    try:
        if MyList[0] in dictionary.keys():
            return DirectoryChecker(MyList[1:],dictionary[MyList[0]])
        else:
            return len(MyList)
    except AttributeError:
        return len(MyList)

temp=list(map(lambda s: s.strip('\n'),temp))
numcases=temp.pop(0)
numcases=int(numcases)

thefile=open(r'C:\Documents and Settings\Me\My Documents\Coding Fun\Google Code Jam\out.txt','w')

pt=0
for j in range(numcases):
    finalcount=0
    BigDict=dict()
    firstline=temp[pt].split(' ')
    N=int(firstline[0])
    M=int(firstline[1])
    pt+=1
    for jj in range(N):
        DirectoryMaker(temp[pt][1:].split('/'),BigDict)
        pt+=1
    for jj in range(M):
        toadd=DirectoryChecker(temp[pt][1:].split('/'),BigDict)
        finalcount+=toadd
        if toadd>0: DirectoryMaker(temp[pt][1:].split('/'),BigDict)
        pt+=1
    thefile.write('Case #'+str(j+1)+': '+str(finalcount)+'\n')
thefile.close()
