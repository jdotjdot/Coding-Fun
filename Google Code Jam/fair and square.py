# Fair and square
import math

infile = open(r'C:\Users\Me\Downloads\C-large-1.in', 'r')
#infile = open(r'C:\in.txt', 'r')
text = infile.read().split('\n')
text = text[1:]
##for index, content in enuermate(

# finish this piece
outfile = open(r'C:\out.txt', 'w')


def is_palindrome(x):
    t = str(x)
    for num in range(0, len(t)/2):
        if t[num] != t[-(num+1)]:
            return False
    else:
        return True
            
def is_sqrt(x):
    return math.sqrt(x) % 1 == 0

##for x in range(A, B+1):
##    if str(x) == str(x)[::-1]:
##        if math.sqrt(x) % 1 == 0:
##            out += 1
##
##
##for x in range(A, B+1):

current_case=1
for row in text:
    if row == '': continue
    A, B = map(int, row.split(' '))

    out = 0
    for x in xrange(long(A), long(B+1)):
        if is_sqrt(x):
            current_root = int(math.sqrt(x))
            break

    while current_root**2 <= B:
        if is_palindrome(current_root):
            if is_palindrome(current_root**2):
                out+=1
        current_root += 1

    outfile.write('Case #{}: {}\n'.format(current_case, out))
    current_case += 1

outfile.close()
