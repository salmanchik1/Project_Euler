# This program is written in Python 3.7
coins = [1, 2, 5, 10, 20, 50, 100, 200]  # This loop should be sorted
sum_pence = 200


def calc_combinations(value, coin):  # value - the sum of coins, the number of biggest coin in the list
    """This recursive function calculates the amount of different coin combinations"""
    if coin == 0:  # the smallest coin gives us just one combination
        return 1   # even though if we are not needed more coin to fill the sum
    return sum(calc_combinations(value - coins[coin] * i, coin - 1)  # subtract the sum of the coins #coin
               for i in range(value // coins[coin] + 1))
    # run i from 0 to the amount of coins which fit into the value


print(calc_combinations(sum_pence, len(coins) - 1))
