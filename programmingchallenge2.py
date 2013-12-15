def __init__():
    print('''Programming-Challenge-2 J.J. Fliegelman

    At least starting off with this now, this strikes me as a
    a textbook example of the knapsack problem.  I'll start
    with that on a smaller scale, and then see how that scales
    when we go up to 70 users.

    As we scale to 70 people, it becomes clear quickly that those with bigger
    balances and with accounts at banks with smaller rebates are going to have
    to wait longer to have their accounts settled.  When adding complexity to
    this problem to take into account ''')

###Do some actual testing, testing with both 70 people for that night
### as well as doing that across many nights, with new account holders

from operator import truediv

class User:
    def __init__(self, balance, bank):
        '''balance -> balance input
bank -> bank input
rebate(bank) -> returns the fixed rebate provided by that bank'''
        self.balance = balance
        self.bank = bank
        self.__rebate(bank)
    def __rebate(self, bank):
        if bank == 'BofA':
            self.rebate = 2.32
        elif bank == 'WFC':
            self.rebate = .73
        elif bank == 'Chase':
            self.rebate = 2.01
        elif bank == 'M&T':
            self.rebate = .50
        elif bank == 'BB&T':
            self.rebate = 1.41
        elif bank == 'First National':
            self.rebate = .79
        elif bank == 'PNC':
            self.rebate = .48
        elif bank == 'HSBC':
            self.rebate = .38
        elif bank == 'Bank of the West':
            self.rebate = 1.33
        else:
            raise ValueError
    def rebate_per_balance(self):
        return truediv(self.rebate, self.balance)
        # truediv used for Python 2.7 compatibility

def InputDataSet__():
    return [(153.00, 'BofA'), (53.00, 'WFC'), (191.00, 'Chase'),
            (66.05, 'M&T'), (239.99, 'BB&T'),
            (137.55, 'First National'), (145.78, 'PNC'),
            (249.43, 'HSBC'), (43.01, 'Bank of the West')]

def UsersetMaker(userlist):
    return [User(x[0], x[1]) for x in userlist]

def LoadKnapsack(userlist, maxsettlement):
    userlist.sort(key = lambda x: x.rebate_per_balance(),
                  reverse = True)
    knapsack = []
    while sum([x.balance for x in knapsack]) <= maxsettlement and \
          len(userlist) > 0:
        if userlist[0].balance <= maxsettlement - \
           sum([x.balance for x in knapsack]):
            knapsack.append(userlist.pop(0))
        else:
            userlist=userlist[1:]
    return knapsack

def Main():
    userlist = UsersetMaker(InputDataSet__())
    return LoadKnapsack(userlist, 645)
    pass

if __name__ == "__main__":
    Main()
