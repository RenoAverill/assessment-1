import math
# Declare optimal_change function that takes in two params(item_cost, amount_paid)
def optimal_change(item_cost, amount_paid):

    # define a varriable to get total change that is due
    change_due = amount_paid - item_cost

    # define a result string 
    end_of_transaction = (f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is ")

# create a list of amount of money and count of how many
    money_list = [
        [100, 0],
        [50, 0],
        [20, 0],
        [10, 0],
        [5, 0],
        [1, 0],
        [0.25, 0],
        [0.10, 0],
        [0.05, 0],
        [0.01, 0]
    ]

    # create instance to see if money is still owed and inform buyer
    if change_due < 0:

        # declare vairable for money that is still needed
        money_still_required = (item_cost - amount_paid)
        print (f"Please add ${money_still_required} to complete transaction!")
        return
    

    # # loop through list indexes and make and amount variable
    for list in money_list:
        amount = list[0]
            
        # count how many times a bill or coin is needed to be refunded
        while round(change_due, 3) >= amount:
            list[1] += 1
            change_due -= amount

    # loop through money list and add correct puncuation to end statement
    for list in money_list:

        # decalse singular and plural varriables to use later for correct puntuation
        singular = list[1] == 1
        plural = list[1] > 1

        # see if a bill or coin needs to be refunded
        if list[1] > 0:
            end_of_transaction += (f"{list[1]} ${list[0]} ")

            # create a list compiled of values of their bills
            list_of_bills = [100,50,20,10,5,1]

            # create a list compiled of sub lists that have the values and names of coins
            list_of_coins = [[0.25, 'quater'], [0.10, 'dime'], [0.05, 'nickle'], [0.01, 'penny']]

            # 
            if list[0] in list_of_bills:
                if singular:
                    end_of_transaction += 'bill, '
                if plural:
                    end_of_transaction += 'bills, '

            # loop though and find what bill or coin is singular or plural
            for coin_list in list_of_coins:
                if list[0] in coin_list :
                    if singular:
                        if coin_list[0] == 0.25:
                            end_of_transaction += 'quarter, '
                        elif coin_list[0] == 0.10:
                            end_of_transaction += 'dime, and '
                        elif coin_list[0] == 0.05:
                            end_of_transaction += 'nickle, '
                        elif coin_list[0] == 0.01:
                            end_of_transaction += 'penny.'
                    if plural:
                        if list[0] == 0.25:
                            end_of_transaction += 'quarters, '
                        elif list[0] == 0.10:
                            end_of_transaction += 'dimes, and '
                        elif list[0] == 0.05:
                            end_of_transaction += 'nickles, '
                        elif list[0] == 0.01:
                            end_of_transaction += 'pennies.'

       
    
    return(end_of_transaction.replace('$0.01 ','').replace('$0.05 ','').replace('$0.1 ','').replace('$0.25 ',''))

# print(optimal_change(10, 11.23))
