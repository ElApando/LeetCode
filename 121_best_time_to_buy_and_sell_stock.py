"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different
 day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit,
 return 0.


Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

from typing import List

def max_profit(ls_prices: List[int]) -> int:
    """ Obtiene el mejor momento pra comprar una acción
    
    Parameters:
        - ls_prices *(list)* - Lista con los precios de la accción
    Returns:
        - in_max_value *(list)* - Ganancia máxima al ven der la acción
    """

    in_min_value = ls_prices[0]
    in_max_value = 0

    for jj in range(0,len(ls_prices),1):
        in_min_value = min(in_min_value, ls_prices[jj])
        in_max_value = max(in_max_value, ls_prices[jj] - in_min_value)
        print(jj, ls_prices[jj], in_min_value, in_max_value, ls_prices[jj] - in_min_value)

    return in_max_value

ls_prove = [[7,1,5,3,6,4],[7,6,4,3,1]]
print([max_profit(ii) for ii in ls_prove])

# Finite Incantatem
