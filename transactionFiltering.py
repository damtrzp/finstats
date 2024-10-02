from typing import List
from main import Transaction


def transactionsInDateRange(transactionList : List[Transaction], minDate = 0, maxDate = 99999999999999999999999999):
    newTransactions = []
    for transaction in transactionList:
        if transaction.transactionDateEpoch <= maxDate and transaction.transactionDateEpoch >= minDate:
            newTransactions.append(transaction)
    return newTransactions