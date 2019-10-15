# P9-Stock-Market-Simulator
CS301-9
Program Skills
Creating and managing dictionaries
More practice with functions and iteration
Summary
We are creating a program to manage (very basic, not actually real) stock trading. On each day, an account holder can: do nothing, buy some shares of a particular stock, or sell some shares of a stock. However: stock prices will change randomly every day, and the transaction will not take place until AFTER they change! So exciting.

Be aware: this writeup is lengthy because we want you to focus on the data management portion of the program, not the logistics of the algorithms. Seriously, I am trying to help you.

Read this writeup carefully before you begin.

Program Requirements
For this assignment, you should write five (5) functions with the following behaviors and names:

buy(transactions, holder_name, company_name, num_shares) - validates the arguments and, if valid, adds the transaction to the transactions list.
sell(transactions, holder_name, portfolio, company_name, num_shares) - validates the arguments and, if valid, adds the transaction to the transactions list.
update_prices(stocks) - for each company, randomly adjusts the stock as a percentage of its current price.
update_accounts(account_list, transactions, stocks) - updates each account following their daily transaction.
main() - creates accounts and initial stock prices, then prompts each stockholder for their daily action, updates stock prices, and updates account information accordingly.
These functions are actually pretty simple - I promise. The big piece here is wrapping your head around the multi-tiered data organization:

stocks: a dictionary with company names as keys and stock prices as values. {company_name1: price1, company_name2: price2...}
account_list: a dictionary with account names as keys and portfolios (see below) as values. {holder_name1: {...}, holder_name2: {...} ...}
portfolio: a per-account dictionary, with the company names of stocks owned as keys and the number of shares owned as values. Should also include a 'profit' key, with a value that increases when stocks are sold and decreases when stocks are purchased (may be negative). {stock1: num_shares, stock2: num_shares, ... 'profit': ### }
transactions: a dictionary with account names as keys and actions as values. {holder_name1: ['buy', company_name1, num_shares], holder_name2: ['sell', company_name2, num_shares] ...}
1. Buy shares
The arguments to this function are the transactions dictionary, the account name, the company name, and the number of shares requested. If the number of shares is an integer greater than zero, add the action to the transactions dictionary - no return necessary (transactions is a shallow copy!). If the number of shares is not an integer (or is less than or equal to 0), do not change the transactions dictionary.

>>> transactions = {}
>>> buy(transactions, 'Geoff', 'ANF', 5)
>>> print transactions
{'Geoff':['buy', 'ANF', 5]}
>>> buy(transactions, 'Bob', 'HSY', -4.7)
>>> print transactions
{'Geoff':['buy', 'ANF', 5]}
2. Sell shares
The arguments to this function are the same as for buying, except we also include the holder's portfolio. In this case, we want to verify that the number of shares is not only an integer greater than zero, but also less than or equal to the number of shares that this holder currently owns. If the number of shares is valid, add the action to the transactions dictionary as in buy().

>>> transactions = {}
>>> folio = {'profit':0, 'ANF':5, 'HSY': 1}
>>> sell(transactions, 'Geoff', folio, 'ANF', 3)
>>> print transactions
{'Geoff':['sell', 'ANF', 3]}
>>> sell(transactions, 'Bob', folio, 'HSY', 3)  # folio does not contain sufficient HSY stock
>>> print transactions
{'Geoff':['sell', 'ANF', 3]}
3. Update prices
This function should randomly fluctuate the price of each stock in our stocks dictionary as a percent of that stock price.

For every stock in the stock dictionary, generate a random number using a normal distribution (Links to an external site.) with mean 0 and standard deviation 0.1 (a 10% change). Multiply this by the stock's current price, and add that amount to the current price of the stock. This is the stock's new value.

>>> stocks = {'ANF': 68.81, 'HSY': 80.28, 'AAPL': 94.82}
>>> for i in range(10):
...     update_prices(stocks)
...     print stocks
...
{'ANF': 69.85830145485478, 'HSY': 89.36841509118317, 'AAPL': 92.39472726826679}
{'ANF': 57.48285432714967, 'HSY': 89.70679703931079, 'AAPL': 95.63357547644699}
{'ANF': 56.79907462662556, 'HSY': 73.09881506873452, 'AAPL': 91.29401399676492}
{'ANF': 49.54034684776951, 'HSY': 74.14080717141339, 'AAPL': 105.922264805013}
{'ANF': 47.854837760408124, 'HSY': 65.52659181053126, 'AAPL': 95.8457762236949}
{'ANF': 54.006583643122994, 'HSY': 70.00042617659369, 'AAPL': 106.64698373028904}
{'ANF': 57.94497677971463, 'HSY': 72.67289199889817, 'AAPL': 122.37608203451265}
{'ANF': 52.81832650473787, 'HSY': 64.68387496595838, 'AAPL': 118.0319038954446}
{'ANF': 48.445118237310325, 'HSY': 55.480771179775296, 'AAPL': 133.5724306714933}
{'ANF': 49.915148121169956, 'HSY': 50.566930631100746, 'AAPL': 136.7077122505043}
(Note that this is happening randomly, so your output won't match this exactly.) You should not return anything from this function; all changes should be made using a shallow copy of the dictionary.

4. Update accounts
 This function is slightly tricky because you're wrangling a bunch of nested data. Use temporary variables! This is an example of where shallow copy/nicknaming can come in handy:

account_list[account_name][transactions[account_name][1]]
is a LOT of square brackets. But if you say something like

action = transactions[account_name]     # the transaction we're considering
company_name = action[1]                # the company name associated with the transaction
portfolio = account_list[account_name]  # the account dictionary for the transaction account

portfolio[company_name]
that's SO much easier to read and understand!

So with that in mind, here is what this function should do:

For every account associated with a transaction in the transactions dictionary:
If the account's action is "buy", add the requested number of shares to that account's dictionary entry for that company. (If the company is not yet in the dictionary, add it to their dictionary.) Subtract the total cost of those shares from that account's "profit" entry.
If the account's action is "sell", subtract the requested number of shares from that account's dictionary entry for that company. Add the total cost of those shares to that account's "profit" entry.
And that's it! You don't even need to do any validation, since all values should be validated before they are added to the transactions dictionary.

>>> accounts = {'Geoff':{'profit':-1000, 'AAPL':20}}
>>> transactions = {'Geoff':['sell','AAPL',5]}
>>> stocks = {'AAPL':52, 'ANF':4, 'HSY':64}
>>> update_accounts(accounts, transactions, stocks)
>>> print accounts
{'Geoff':{'profit':-740, 'AAPL':15}}
5. Main function
Your main function runs the interactive simulation.

First, create initial stock prices for at least three companies in your stocks dictionary. I did this randomly; you can do that or hard-code initial values if you like.

Second, create empty accounts (with a 0-profit entry) for at least three stockholders. You may name them whatever you like.

Finally, run the simulation as follows:

Print all of the companies and their current stock prices.
Give each stockholder the option to (1) buy, (2) sell, or (3) do nothing.
If they buy, ask which company and how many stocks.
If they sell, show them their current holdings, then ask which company and how many stocks.
Update the stock prices.
Update the accounts - using the new prices! (The stock market is brutal.)
Show each holder's current profit.
Repeat from step 1.
See below for sample output. Remember you can interrupt an infinite loop on the command line using control+C (on every operating system).

Note that we will NOT require you to do any input checking in this function. You are welcome to include it if you'd like the practice, but we want to focus on correctly managing data in this program, not dealing with typos. You may assume all user inputs here are valid.

Sample Output
This program should run as follows:

STOCK EXCHANGE SIMULATOR

ANF: 54.2112927296
HSY: 67.970947625
AAPL: 35.9296404044

1. Buy
2. Sell
3. Nothing

A, what would you like to do: 1
Which company? AAPL
How many stocks? 20
B, what would you like to do: 1
Which company? ANF
How many stocks? 10
C, what would you like to do: 3

A -823.948506914
B -614.839143288
C 0

ANF: 61.4839143288
HSY: 60.9347652852
AAPL: 41.1974253457

1. Buy
2. Sell
3. Nothing

A, what would you like to do: 1
Which company? HSY
How many stocks? 5
B, what would you like to do: 2
ANF: 10
Which company? ANF
How many stocks? 5
C, what would you like to do: 1
Which company? AAPL
How many stocks? 10

A -1177.70155974
B -314.497209954
C -412.676120708

ANF: 60.0683866667
HSY: 70.7506105654
AAPL: 41.2676120708

1. Buy
2. Sell
3. Nothing

A, what would you like to do: 2
AAPL: 20
HSY: 5
Which company? HSY
How many stocks? 5
B, what would you like to do: 3
C, what would you like to do: 2
AAPL: 10
Which company? AAPL
How many stocks? 5

A -858.955621627
B -314.497209954
C -193.887423203

ANF: 67.338004166
HSY: 63.7491876229
AAPL: 43.757739501

1. Buy
2. Sell
3. Nothing

A, what would you like to do: 3
B, what would you like to do: 2
ANF: 5
Which company? ANF
How many stocks? 5
C, what would you like to do: 1
Which company? ANF
How many stocks? 5

A -858.955621627
B 36.9707452213
C -545.355378379

ANF: 70.2935910351
HSY: 71.9501907204
AAPL: 45.1445000998

1. Buy
2. Sell
3. Nothing

A, what would you like to do: ...
Commenting Your Code
As with last week's program, every function you write is required to include a docstring, and you must also write comments in your code.

Handing In Your Program
Students completing this program in pairs should join a P9 Group. If you are having trouble joining (not creating!) a P9 Group, please contact Hobbes with your partner's name.

When you're done, upload all functions in a file called stockmarket_hw.py.
