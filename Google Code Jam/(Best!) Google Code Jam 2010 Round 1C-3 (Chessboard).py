## Google Code Jam 2010 Round 1C-C Making Chess Boards
# 7/22/2010
#Uses NumPy for matrix stuff
#Speed problem here is definitely Python.  Even using the algorithm
#that Google provides as the answer, only slightly off from mine,
#with O(n*m*log(n*m)), still taking awy too long.
#For future practice, I'll have to learn C, C++, and/or Java.

#Please note that due to some colossal stupidity, x's usually refer
#to the ROW, and y's refer to the COLUMN--so it makes sense in terms of
#Matlab, but if you are looking at it from a graphing perspective,
#x and y are reversed.

import numpy as np
import weakref
import itertools
import operator
import time,sys

def comb(a):
	if len(a[0])==len(a[1]):
		return [(a[0][n],a[1][n]) for n in range(len(a[0]))]
	else:
		raise TypeError

class ChessBoard:
    r"""StartX,StartY,SideLength,base
    Well, this will be fun, won't it?
    x1 and y1 - top-left coordinates
    x2 and y2 - bottom-right coordinates
    side - length of a side of the square
    ix - index range for slicing use out of the bigger bark
    """
    def __init__(self, StartX=0, StartY=0, SideLength=1, base=None):
        self.x1=StartX
        self.y1=StartY
        self.side=SideLength
        self.size=self.side
##        self.ix=np.ix_(list(range(self.x1,self.x1+self.side)),
##                       list(range(self.y1,self.y1+self.side)))
        self.base=weakref.proxy(base)
    def ix(self):
        return np.ix_(list(range(self.x1,self.x1+self.side)),
                      list(range(self.y1,self.y1+self.side)))
    def layout(self):
        '''This method returns a proxy to the base trunk.
        It WILL change as trunk changes!'''
        return self.base[self.ix()]
    def firstcolor(self):
        #Make sure this is a horizontally-based matrix
        return self.base[self.y1][self.x1]
    def CheckIfBoard(self):
        return CheckIfBoard(self.x1,self.y1,self.side,self.base)
    def coordinates(self):
        return tuple(itertools.chain(*(list(itertools.product(*k)) for k in itertools.product(*self.ix(self)))))
    def test(self):
        return 'hello world!'

def CheckIfBoard(x,y,side,trunk):
    def CheckEqual(lst):
        return lst[1:]==lst[:-1]
    def CheckAlongLine(lst):
        tmp=lst[0]
        if tmp not in [0,1]: return False
        for a in lst[1:]:
            tmp=abs(tmp-1)
            if tmp!=a:
                return False
        else:
            return True
    #trunk should be as np.array
    sample=trunk[x:x+side,y:y+side]
    x0=list(sample.sum(axis=0))
    x1=list(sample.sum(axis=1))
##    if len(x0)>1 and len(x0)<=5:
##    try:
    for xy in range(len(x0)):
        if not all([CheckAlongLine(sample[xy,:]),CheckAlongLine(sample[:,xy])]):
            return False
    else:
        return True
##        except IndexError:
##            return False
##    elif len(x0)>1:
##        return all((
##            abs(x0[0]-x0[1])==1, #the alternating pattern is exactly 1 different
##            x0[::2]==x1[::2], #every other x sum equal to every other y sum
##            x0[1::2]==x1[1::2], #ditto for the missing other
##            CheckEqual(x0[::2]), #check to make sure that the altnernatings are the same
##            CheckEqual(x0[1::2]),
##            CheckEqual(x1[::2]),
##            CheckEqual(x1[1::2])
##            ))
##    else:
##        return True

dirpath=r'C:\Documents and Settings\Me\My Documents\Coding Fun\Google Code Jam'
with open(dirpath+r'\in.txt','r') as it:
    temp=it.readlines()

numcases=int(temp.pop(0).strip('\n'))

pt=0
finaloutput=[]
for i in range(numcases):
    #M rows, N columns
    M,N=map(int,temp[pt].strip('\n').split(' '))
    pt+=1
    bigbark=[]
    for ii in range(M):
        bigbark.append(bin(int(temp[pt].strip('\n'),16))[2:].zfill(N))
        pt+=1
    #print('finished bigbark' + time.asctime(time.localtime()))
    trunk=np.array([[int(char) for char in line] for line in bigbark])
    allboards=[]
    
    for Y in range(N):
        for X in range(M):
            #if i>96: print(str(i)+' - ('+str(X)+','+str(Y)+')')
            size=1
            #The next 6 lines should really be a function
            while X+size-1<M and Y+size-1<N:
                
                if CheckIfBoard(X,Y,size,trunk):
                    if X+size==M or Y+size==N:
                            allboards.append(ChessBoard(X,Y,size,trunk))
                            break
                    else:
                            size+=1
                else:
                    allboards.append(ChessBoard(X,Y,size-1,trunk))
                    break

    allboards.sort(key=lambda x: (x.side*-1,x.x1,x.y1))

    
    boardnum=2
    case={}
    
    while len(allboards)>0:
            #if i>96: print(str(i)+' - '+str(boardnum))
            board=allboards[0]
            if (board.layout()<2).all():
                if board.side in case.keys():
                    case[board.side]+=1
                else:
                    case[board.side]=1
                trunk[board.ix()]=boardnum
                boardnum+=1
                del allboards[0]
            else:
                #Basically the biggestsquare "function" but starting with largest size
                if board.layout()[0,0]>1:
                        del allboards[0]
                else:
                        for newsize in range(board.side-1,0,-1):
                            if CheckIfBoard(board.x1,board.y1,newsize,trunk):
                                allboards[0].side=newsize
                                break
            allboards.sort(key=lambda x: (x.side*-1,x.x1,x.y1))

    #Now, write to outputholder!
    finaloutput.extend(['Case #'+str(i+1)+': '+str(len(case.keys()))])
    finaloutput.extend([str(key)+' '+str(val) for key,val in sorted(list(case.items()),key=operator.itemgetter(0),reverse=True)])
    
    
#########################
##    ATTEMPT 2
#########################
##    boardnum=2
##    case={}
##    for size in range(min([N,M]),1,-1):
##        print('finished size ' +str(size) + ' ' + time.asctime(time.localtime()))
##
##        for X,Y in comb([list(q) for q in np.nonzero(trunk<2)]):
##          if X+size-1<M and Y+size-1<N:
##            #while X+size-1<M: #while Y+size-1<N:
##            #print(str(size)+' - '+str(X)+','+str(Y))
##            if CheckIfBoard(X,Y,size,trunk):
##                #change on trunk
##                tp=ChessBoard(X,Y,size,trunk)
##                trunk[tp.ix()]=boardnum
##                boardnum+=1
##                
##                #add to output
##                if size in case.keys():
##                    case[size]+=1
##                else:
##                    case[size]=1
##            
##    po=len(trunk[np.nonzero(trunk<2)])
##    if po>0: case[1]=po
##    del po
##
##    #Now, write to outputholder!
##    finaloutput.extend(['Case #'+str(i+1)+': '+str(len(case.keys()))])
##    finaloutput.extend([str(key)+' '+str(val) for key,val in sorted(list(case.items()),key=operator.itemgetter(0),reverse=True)])

###########################
##    ATTEMPT 1
###########################    
##    for Y in range(N):
##        for X in range(M):
##            size=2
##            while X+size-1<M and Y+size-1<N:
##                if CheckIfBoard(X,Y,size,trunk):
##                    allboards.append(ChessBoard(X,Y,size,trunk))
##                else:
##                    break
##                size+=1
##    print('finished allboards'+time.asctime(time.localtime()))
##    ## Now that we have all the possible boards, time to start ranking and taking
##    allboards.sort(key=lambda x: (x.side*-1,x.x1,x.y1))
##
##    ## Done that--now time to start sorting through
##    #Was going to try a list of used coordinates, but I think I'll actually just use trunk now
##    #I'll even clearly number each board on trunk!
##    boardnum=2
##    case=dict()
##    #I'm pretty pleased with this method I've chosen to finish up,
##    #it's much more elegant and efficient than what I had originally
##    #thought of
##    for board in allboards:
##        if (board.layout()>1).any():
##            #Any coordinate is not 0 or 1, ie has been used
##            #allboards.remove(board)
##            pass
##        else:
##            trunk[board.ix()]=boardnum
##            boardnum+=1
##            if board.side not in case.keys():
##                case[board.side]=1
##            else:
##                case[board.side]+=1
##    po=len(trunk[np.nonzero(trunk<2)])
##    if po>0: case[1]=po
##    del po
##    print('finished running boards'+time.asctime(time.localtime()))
##
##    #Now, write to outputholder!
##    finaloutput.extend(['Case #'+str(i+1)+': '+str(len(case.keys()))])
##    finaloutput.extend([str(key)+' '+str(val) for key,val in sorted(list(case.items()),key=operator.itemgetter(0),reverse=True)])

with open(dirpath+r'\out.txt','w') as outputfile:
    outputfile.write('\n'.join(finaloutput))

