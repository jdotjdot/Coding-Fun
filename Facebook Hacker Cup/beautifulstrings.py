import string, operator, random
from collections import Counter

def get_file(filename):
    infile = open(filename, 'r')
    lines = [x.strip() for x in infile.readlines()]
    return lines

def calculate_beauty(mystring):
    mystring = ''.join(letter for letter in mystring.lower() if letter in string.ascii_lowercase)
    c = Counter(mystring)
    sort = sorted(c.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sum(map(lambda x: x[0]*x[1][1], zip(range(26,0,-1), sort)))



def main():
    infile = open(r'C:/Users/JJ Fliegelman/Downloads/beautiful_stringstxt.txt', 'r')
##    infile = open(r'C:/FB/input.txt', 'r')
    infile.next()
    with open(r'C:/FB/out.txt', 'w') as outfile:
        for index, line in enumerate(infile):
            print line
            print 'Case #{}: {}\n'.format(index+1, calculate_beauty(line))
    infile.close()
    print 'Done!'
   
if __name__ == '__main__':
    main()
