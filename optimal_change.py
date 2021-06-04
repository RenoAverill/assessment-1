
# Declare optimal_change function that takes in two params(item_cost, amount_paid)
def optimal_change(item_cost, amount_paid):

    # define a function to get total change that is due
    def change_due(amount_paid, item_cost):
         return amount_paid - item_cost

    # define a result string 
    end_of_transaction = ''

# create a list of dictionaries for different dollars and coins with corresponding name
    money_list = [
        {100: 'bill'},
        {50: 'bill'},
        {20: 'bill'},
        {10: 'bill'},
        {5: 'bill'},
        {1: 'bill'},
        {.25: 'quarter'},
        {.10: 'dime'},
        {.05: 'nickle'},
        {.01: 'penny'}
    ]
    # create instance to see if money is still owed and inform buyer
    while change_due() < 0:
        # declare vairable for money that is still needed
        money_still_required = (item_cost - amount_paid)
        print (f"Please add ${money_still_required} to complete transaction!")
    # loop through list
    for money_obj, money in enumerate(money_list):
        # declare vaiable for amount of money in each individual obj
        amount = money_list[money_obj][0]
        while change_due > amount:
            # add amount to end_of_transaction report
            end_of_transaction += amount
            # subtract the amount of change that is due by the amount paid out to customer
            change_due -= amount
    # Print return string with optimal change w/ the following convention
    print(end_of_transaction)
print(optimal_change(62.13, 100))


# optimal_change(62.13, 100)
# > "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

# optimal_change(31.51, 50)
# > "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."