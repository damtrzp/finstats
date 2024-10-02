from typing import List
from main import Transaction, dictToBarChart


"""

"""

# The function calculates spending of a given amount and
# optionally it's increments for each counterparty
def exactAmountSpendingByCounterparties(allTransactions : List[Transaction], amount : float, includeIncrements : bool = False, maxAmount = 100):
    result = {}
    for transaction in allTransactions:
        amountSpent = -transaction.amount
        # Check if the money was spent and not obtained and check if the money falls into max amount
        if amountSpent < 0 or amountSpent > maxAmount:
            continue

        shouldAdd = False
        if includeIncrements:
            if amountSpent % amount == 0:
                shouldAdd = True
        elif amountSpent == amount:
            shouldAdd = True
        if shouldAdd:
            if transaction.counterparty not in result:
                result[transaction.counterparty] = amountSpent
            else:
                result[transaction.counterparty] += amountSpent
    dictToBarChart(result)

def SpendingByCounterparties(allTransactions : List[Transaction], maxAmount = 99999, minimumTotal : float = 0):

    result = {}
    for transaction in allTransactions:
        amountSpent = -transaction.amount
        # Check if the money was spent and not obtained and check if the money falls into max amount
        if amountSpent < 0 or amountSpent > maxAmount:
            continue

        if transaction.counterparty not in result:
            result[transaction.counterparty] = amountSpent
        else:
            result[transaction.counterparty] += amountSpent
        # Threshold
    for key in list(result):
        if result[key] < minimumTotal:
            del result[key]
    dictToBarChart(result)