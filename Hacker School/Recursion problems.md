
Write a naive fibinacci function recursively. It should look a lot like below,
but you'll need to add some code: (Bonus for later: memoize this) Explain it to
someone else.


    def fib(n):
        if n<2:
            return n
        else:
            return fib(n-2) + fib(n-1)


    [fib(x) for x in range(10)]




    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]



Warm up: using no loops (for, while, etc.), and no global variables, write a
function that returns the sum of a list: Also, no cheating and calling methods
that do significant work for you (i.e. sum(), reduce(), etc. are all off
limits).


    def sumlist(thelist, acc=0):
    	if thelist == []:
    		return acc
    	else:
    		return sumlist(thelist[1:], acc + thelist[0])


    sumlist([4,5,6,7])




    22



Again, using no loops, no global variables, no calling len() and no helper
functions write a function that returns the last index of a given input in a
list. Negative one gets returned if the element doesn't occur in the list.



    def lastIndexOf(n, thelist, acc=-1, counter=0):
        if thelist == []:
            return acc
        else:
            return lastIndexOf(n, thelist[1:],
                               acc=counter if thelist[0]==n else acc,
                               counter=counter + 1)


    lastIndexOf(5, [1, 2, 4, 6, 5, 2, 5, 7])




    6



Try the same thing for a linked list:


    def linkedLastIndexOf(n, thelist, acc=-1, counter=0):
    	if not thelist:
    		return acc
    	else:
    		return linkedLastIndexOf(n, thelist[1],
    					 counter if thelist[0]==n else acc,
    					 counter + 1)


    linkedLastIndexOf(5, [1,[2,[4,[6,[5,[2,[7,None]]]]]]])




    4




    lastIndexOf(5, [1, [2, [4, [6, [2, [7, None]]]]]])




    -1



Write a recursive function to compute the sum of a list of numbers.


    def recursive_sum(thelist, acc=0):
    	if thelist == []:
    		return acc
    	else:
    		return recursive_sum(thelist[1:], acc + thelist[0])


    recursive_sum([4,3,7,8,2])




    24



####Word problems
No longer recursion only; now can use whatever tools we like.

Generate all the reorderings of a set of letters.


    def all_reorderings(letters):
        import itertools
        # Was this cheating?
        if type(letters) is list:
            letters = ''.join(letters)
        return itertools.permutations(letters)

List all of the series' of letters (non-dictionary words, 'asd' and 'w' count)
that can be formed with some scrabble tiles on a blank board. (In scrabble, you
don't have to use all your tiles at once)


    def all_reorderings(letters):
        import itertools
        # Cheating again
        
        if type(letters) is list:
            letters = ''.join(letters)
            
        for r in range(1, len(letters) + 1):
            for x in itertools.permutations(letters, r):
                yield ''.join(x)


    g = all_reorderings(['a', 'b', 'c'])
    [g.next() for _ in range(15)]




    ['a',
     'b',
     'c',
     'ab',
     'ac',
     'ba',
     'bc',
     'ca',
     'cb',
     'abc',
     'acb',
     'bac',
     'bca',
     'cab',
     'cba']



List all of the valid words (give some dictionary) that can be formed with some
scrabble tiles on a blank board


    def all_reorderings(letters, dictionary=[]):
        import itertools, collections
        # Cheating...again
        if type(letters) is list:
                letters = ''.join(letters)
        
        c = collections.Counter(letters)
        
        for word in dictionary:
            dictword = collections.Counter(word)
            if all(dictword[x] <= c[x] for x in dictword.keys()):
                yield word


    [x for x in
     all_reorderings('abccccjfffjelfjawefhogellwaeo', dictionary=['chello', 'hello', 'joe', 'jonathan'])]




    ['chello', 'hello', 'joe']



A child is running up a staircase with n steps, and can hop either 1 step, 2
steps, or 3 steps at a time. Write a function that, given the length of the
staircase, tells you how many ways there are to go up the steps.

let n := 11

[  3  ] [  3  ] [  3  ] [ 2 ]
[ 111 ] [ 111 ] [ 111 ] [ 11]
[ 1 2 ] [ 1 2 ] [ 1 2 ] 

... not done

####More recursion practice

Write a recursive implementation of the map function.


    def recursive_map(fn, thelist, acc=[]):
        if not thelist:
            return acc
        else:
            return recursive_map(fn, thelist[1:], acc + [fn(thelist[0])])


    recursive_map(lambda x: x + 1, [4,3,4,5])




    [5, 4, 5, 6]



Write a recursive implementation of the filter function.


    def recursive_filter(fn, thelist, acc=[]):
        if not thelist:
            return acc
        else:
            return recursive_filter(fn, thelist[1:], acc + ([thelist[0]] if fn(thelist[0]) else []))


    recursive_filter(lambda x: x==4, [3,4,5,6,6,5,4])




    [4, 4]



Write a recursive function that inserts an element in the right place into a
linked list. The function should return a new linked list rather than mutate the
original list.


    ###Unfinished
    
    
    g = [('a', 1), ('b', 3), ('d', -1), ('c', 2)]
    
    def recursive_insert_linked_list(insert_item, insert_index, current_item, counter=0, acc=[], linked_list=g):
        # list_init is a tuple of (item, next item location)
        # for exercise purposes, linked list is an entire object within a python list, like 'g' above
        
        if insert_index == counter:
            
        
