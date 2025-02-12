#Nathan Parker
#2/11/25
#Program #5: Bank Balance

#get the monthly budget from the user
accumulator = float(input('Enter the amount that you have budgeted for a month: '))

#get first expense from the user
expense = float(input('Enter an expense for the month: '))

#subtract the new expenses from the accumulator and ask for new expenses until an expense equals 0
while expense != 0:
    accumulator -= expense
    expense = float(input('Enter an expense for the month: '))

#display the balance
print(f'Your balance is ${accumulator:,.2f}.')
