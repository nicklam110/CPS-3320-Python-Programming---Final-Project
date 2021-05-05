usage = '''
Expense Tracker CLI.
Usage:
  expensetracker_exe.py init
  expensetracker_exe.py view [<view_category>]
  expensetracker_exe.py <amount> <category> [<message>]
'''

from docopt import docopt
from expensetracker import *
from tabulate import tabulate

args = docopt(usage)

if args['init']:
    init()
    print("User Profile Created")

if args['view']:
    category = args['<view_category>']
    amount, results = view(category)
    print("Total expense: ", amount)
    print(tabulate(results))

if args['<amount>']:
    try:
        amount = float(args['<amount>'])
        log(amount, args['<category>'], args['<message>'])
    except:
        print(usage)