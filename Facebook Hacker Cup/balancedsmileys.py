import string, re

def isbalanced(instring):
    if  instring == '^$' or \
        re.search(r'^[a-z \:]+$', instring) or \
        re.search(r'^([a-z \:]+)$', instring):
            return True

    ocount = 0
    ccount = 0
    possibleo = 0
    possiblec = 0
    colon = False
    for index, i in enumerate(instring):
        if i not in string.ascii_lowercase + ' :()':
            return False
        elif i == ':':
            colon = True
        elif i == '(':
            if colon:
                possibleo += 1
                colon = False
            else:
                ocount += 1
        elif i == ')':
            if colon:
                possiblec += 1
                colon = False
            else:
                ccount += 1

        if ccount > ocount:
            if ccount > ocount + possibleo:
                return False

    if ocount > ccount:
        if ocount > ccount + possiblec:
            return False
        
    return True

def main():
    infile = open(r'C:/Users/JJ Fliegelman/Downloads/balanced_smileystxt.txt', 'r')
##    infile = open(r'C:/FB/input.txt', 'r')
    infile.next()
    with open(r'C:/FB/out.txt', 'w') as outfile:
        for index, line in enumerate(infile):
            line = line.strip('\n')
            outfile.write('Case #{}: {}\n'.format(index+1, 'YES' if isbalanced(line) else 'NO'))

if __name__ == '__main__':
    main()
