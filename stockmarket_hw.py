import random

def buy(transactions, holder_name, company_name, num_shares):
  """
  The function is to validates the arguments and, if valid, adds the transaction to the transactions list.
  """
  if isinstance(num_shares, int) and num_shares > 0:
   transactions[holder_name] = ['buy', company_name, num_shares]

"""
transactions = {}
buy(transactions, 'Geoff', 'ANF', 5)
print transactions
buy(transactions, 'Bob', 'HSY', -4.7)
print transactions
print
"""

def sell(transactions, holder_name, portfolio, company_name, num_shares):
  """
  The function is to validates the arguments and, if valid, adds the transaction to the transactions list.
  """
  if isinstance(num_shares, int) and num_shares > 0:
    if portfolio[company_name] >= num_shares:
      transactions[holder_name] = ['sell', company_name, num_shares]
"""
transactions = {}
folio = {'profit':0, 'ANF':5, 'HSY': 1}
sell(transactions, 'Geoff', folio, 'ANF', 3)
print transactions
sell(transactions, 'Bob', folio, 'HSY', 3)
print transactions
print
"""

def update_prices(stocks):
  """
  The function is to randomly adjusts teh stock as a percentage of its current price for each company
  """
  for key in stocks:
    stocks[key] += stocks[key] * random.gauss(0, 0.1)
"""
stocks = {'ANF': 68.81, 'HSY': 80.28, 'AAPL': 94.82}
for i in range(10):
  update_prices(stocks)
  print stocks
print
"""

def update_accounts(account_list, transactions, stocks):
  """
  The function is to updates each account following their daily transaction.
  """
  for key in transactions:
    if transactions[key][0] == 'buy':
      if transactions[key][1] in account_list[key]:
        account_list[key][transactions[key][1]] += transactions[key][2]
      else:
        account_list[key][transactions[key][1]] = transactions[key][2]
      account_list[key]['profit'] -= stocks[transactions[key][1]] * transactions[key][2]
    if transactions[key][0] == 'sell':
      account_list[key][transactions[key][1]] -= transactions[key][2]
      account_list[key]['profit'] += stocks[transactions[key][1]] * transactions[key][2]
"""
accounts = {'Geoff':{'profit':-1000, 'AAPL':20}}
transactions = {'Geoff':['sell','AAPL',5]}
stocks = {'AAPL':52, 'ANF':4, 'HSY':64}
update_accounts(accounts, transactions, stocks)
print accounts
print
print
"""

def main():
  """
  The function is to create accounts and initial stock prices, then prompts each stockholder for their daily action, updates stock prices, and updates account information accordingly.
  """
  stocks = {'ANF': 68.81, 'HSY': 80.28, 'AAPL': 94.82}
  account_list = {'A':{'profit':0},'B':{'profit':0},'C':{'profit':0}}
  transactions = {}

  print "STOCK EXCHANGE SIMULATOR"
  print

  while True:
    """
    step 1: print all of the companies and their current stock prices.
    """
    for key in stocks:
      print key + ': ' + str(stocks[key])
    print

    print "1. Buy"
    print "2. Sell"
    print "3. Nothing"
    print

    """
    step 2: Give each stockholder the option to (1) buy, (2) sell, or (3) do nothing.
    """
    for key in account_list:
      choice = int(raw_input(key + ', what would you like to do: '))
      """
      step 3: If they buy, ask which company and how many stocks.
      """
      if choice == 1:
        com = raw_input('Which company? ')
        num = int(raw_input('How many stocks? '))
        buy(transactions, key, com, num)
      """
      step 4: If they sell, show them their current holdings, then ask which company and how many stocks.
      """
      if choice == 2:
        for stock_name in account_list[key]:
          if stock_name != 'profit':
            print stock_name + ": " + str(account_list[key][stock_name])
        com = raw_input('Which company? ')
        num = int(raw_input('How many stocks? '))
        sell(transactions, key, account_list[key], com, num)
    print
    """
    Step 5: Update the stock prices
    """
    update_prices(stocks)
    """
    step 6: Update the accounts - using the new prices!
    """
    update_accounts(account_list, transactions, stocks)
    """
    step 7: Show each holder's current profit.
    """
    for key in account_list:
      print key, account_list[key]['profit']
    print

    transactions.clear()
