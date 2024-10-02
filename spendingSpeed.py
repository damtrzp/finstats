from typing import List

from main import Transaction


def spendingSpeedOfCounterpartyGains(allTransactions : List[Transaction], counterparty : str, spentMargin : float = 0):
    transactions = list(reversed(allTransactions))
    gainAmounts = []
    spendLengths = []
    curSpendLength = 0
    for i, transaction in enumerate(transactions):
        # Check the counterparty and check if the transaction amount is a gain
        if counterparty in transaction.counterparty and transaction.amount > 0:
            gainAmounts.append(transaction.amount - spentMargin)
            print(transaction)
        elif transaction.amount < 0:
            try:
                gainAmounts[0] += transaction.amount
            except IndexError:  # Catch error in case of empty array (one of the cases being finding a spend before a gain)
                continue

            try:
                deltaTime = transactions[i + 1].transactionDateEpoch - transaction.transactionDateEpoch
                curSpendLength += deltaTime
                if gainAmounts[0] <= 0:
                    gainAmounts.pop(0)
                    spendLengths.append(curSpendLength)
                    curSpendLength = 0
            except IndexError:  # Catch deltaTime calculations out of bounds error
                break
    avgInSecs = sum(spendLengths) / len(spendLengths)
    print(f'Average time of spending for {counterparty}: {avgInSecs / 60 / 60 / 24} days')