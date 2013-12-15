import re
import itertools
pl=r'C:\Documents and Settings\Me\My Documents\Coding Fun\Google Code Jam'+'\\'
with open(pl+'in.txt','r') as file:
    temp=file.readlines()

temp2=[]
for k in temp:
    temp2.append(k.strip('\n'))
temp=temp2
del temp2

first=temp.pop(0)
first=first.split(' ')
L=int(first[0])
D=int(first[1])
N=int(first[2])
del first

lang=tuple(temp[:D])

review=temp[D:]
del temp
theRE=re.compile(r'(?:(?<=\()[a-z]{2,}?(?=\)))|(?:[a-z]{1}(?=[a-z\(]))|(?:[a-z]{1}\Z)')
for i,j in enumerate(review):
    review[i]=theRE.findall(j)

with open(pl + 'out.txt','w') as out:
  case=[0]*N
  for RealWord in lang: # all words
      for num, hold in enumerate(review): # all holds
          # using `all` here for lazy evaluation
          if all(letter in hold[RealWord_index] for RealWord_index, letter in enumerate(RealWord)): #1 word vs 1 hold
             case[num]+=1

  for num, k in enumerate(case):
      out.write('Case #' + str(num+1) + ': ' + str(k))
      if num!=len(case)-1:
          out.write('\n')
