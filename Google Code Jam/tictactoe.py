

infile = open(r'C:\Users\Me\Downloads\A-large.in', 'r')
text = infile.read().split('\n')
text = text[1:]
outfile = open(r'C:\out.txt', 'w')

def check_items(inputlist):
    if isinstance(inputlist, basestring):
        inputlist = list(inputlist)

    if 'T' in inputlist:
        inputlist.remove('T')
    if all(sq == 'X' for sq in inputlist):
        print 'X'
        return 'X won'
    elif all(sq == 'O' for sq in inputlist):
        return 'O won'
    else:
        return False

def solve2(w):
    for item in w:
        temp = check_items(item)
        if temp:
            return temp
    for item in range(4):
        temp = check_items([y[item] for y in w])
        if temp:
            return temp
    temp = check_items([item[index] for index, item in enumerate(w)])
    if temp: return temp
    temp = check_items([w[3][0], w[2][1], w[1][2], w[0][3]])
    if temp: return temp

    everything = ''.join(w)
    if '.' in everything:
        return 'Game has not completed'
    else:
        return 'Draw'

def solve(w):
    T=False
    for index, item in enumerate(w):
        if 'T' in item:
            Trow = index
            Tcol = item.index('T')

            
    #Check row
    rowcheck = check_items(w[Trow])
    if rowcheck:
        return rowcheck

    #Check column
    colcheck = check_items([y[Tcol] for y in w])
    if colcheck:
        return colcheck

    #check diagonals
    if Trow == Tcol:
        diag1check = check_items([item[index] for index, item in enumerate(w)])
        if diag1check:
            return diag1check
    elif (Trow, Tcol) in ((3, 0), (2, 1), (1, 2), (0, 3)):
        diag2check = check_items([w[3][0], w[2][1], w[1][2], w[0][3]])
        if diag2check:
            return diag2check
        
    everything = ''.join(w)
    if '.' in everything:
        return 'Game has not completed'
    else:
        return 'Draw'

currentcase = 1
for startline in range(0, len(text), 5):
    thistime = text[startline:startline+4]
    outfile.write('Case #{}: {}\n'.format(currentcase, solve2(thistime)))
    currentcase+=1
outfile.close()
