from functools import partial
from itertools import izip
import csv

# n k
# a b c r

## {{{ http://code.activestate.com/recipes/164740/ (r1)
import sys
def iterslice(sequence, start=None, stop=None, step=1):
    if step == 0:
        raise ValueError, "Attempt to use 0 as step value"
    if stop is None:
        stop = sys.maxint*cmp(step,0)
    elif stop<0: 
        try:
            stop = max(len(sequence)+stop,0)
        except TypeError:
            raise TypeError, "Negative slice index on unsized sequence"
    if start is None:
        if step>0: 
            start = 0
        else:
            try:
                start = len(sequence)-1
            except TypeError:
                raise TypeError, ("Unable to start from the end of an "
                                  "unsized sequence")
    elif start<0: 
        try:
            start = max(len(sequence)+start,0)
        except TypeError:
            raise TypeError, "Negative slice index on unsized sequence"
    try:
        for i in xrange(start, stop, step):
                yield sequence[i]
    except IndexError:
        return
    except TypeError:
        if step<0:
            raise TypeError, ("Attempt to use negative step on an "
                              "unindexable sequence")
        #check if the sequence support iterator protocol
        itr = iter(sequence)
        try:
            for i in xrange(start):
                itr.next()
            while start<stop:
                yield itr.next()
                for i in xrange(step-1):
                    itr.next()
                start+=step
        except StopIteration:
            return

def general_m(i, a, b, c, r):
    if i == 0:
        return a
    else:
        return ((b*general_m(i-1, a, b, c, r) + c) % r)

def get_k(k, a, b, c, r):
    
    return [general_m(i, a, b, c, r) for i in range(k)]

##class mm(object):
##    def __init__(self, a, b, c, r):
##        self.

def get_min_nonneg_int(sofar):
    s = sorted(sofar)
    for index, item in enumerate([0] + s):
        try:
            for y in range(item + 1, s[index]):
                return y
        except IndexError:
            return s[-1]+1

def get_min_loop(sofar):
    x = get_min_nonneg_int(sofar)
    yield x
    for y in get_min_loop(sofar[1:] + [x]):
        yield y
        
##    s = sorted(sofar)
##    for index, item in enumerate(s):
##        if index == len(s) - 1:
##            while True:
##                yield item
##                item += 1
##        elif index == 0:
##            for subitem in range(1, item):
##                yield subitem
##        else:
##            diff = range(item+1, s[index+1])
##            for subitem in diff:
##                yield subitem

def get_nth_value(n, k, sofar):
    a=0
    newn = n - k
    e = []
    for x in get_min_loop(sofar):
        a+=1
        e.append(x)
        if a == newn:
            print 'minlist:' +str(e)
            print 'len k+minlist:' + str(len(sofar)+len(e)) + ', n:' + str(n)
            break
    a=0
    for x in get_min_loop(sofar):
        a+=1
        if a == n:
            return x

def doit(n, k, a, b, c, r):
##    m = partial(general_m, a=a, b=b, c=c, r=r)
##    global thelist
    thelist = get_k(k, a, b, c, r)
    print thelist
    print len(thelist)
    print 1 in thelist
##    global x
##    x = get_min_nonneg_int(thelist)
##    for x in range(1, n+1):
##        print get_nth_value(x, thelist)
    return get_nth_value(n, k, thelist)
    
def main():
    #infile = open(r'C:/Users/JJ Fliegelman/Downloads/find_the_mintxt.txt', 'r')
    infile = open(r'C:/FB/input.txt', 'r')
    lines = list( csv.reader(infile, delimiter=' ') )
    with open(r'C:/FB/out.txt', 'w') as outfile:
        for index, (line1, line2) in enumerate(izip(lines[1::2], lines[2::2])):
            #if index == 1:
                n, k = map(int, line1)
                a, b, c, r = map(int, line2)
                outfile.write('Case #{}: {}\n'.format(index+1, doit(n,k,a,b,c,r)))

if __name__ == '__main__':
    main()
