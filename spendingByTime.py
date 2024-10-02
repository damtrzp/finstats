from typing import List
import matplotlib.pyplot as plt
from main import Transaction, getDayOfWeekFromEpoch

weekdayNames = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

def spendingByDayOfWeek(allTransactions : List[Transaction], maxAmount : float):
    spendings = [0,0,0,0,0,0,0]
    for transaction in allTransactions:
        amountSpent = transaction.amount
        if 0 < amountSpent < maxAmount:
            weekday = getDayOfWeekFromEpoch(transaction.transactionDateEpoch)
            print(weekday)
            spendings[weekday] += amountSpent
    plt.bar(weekdayNames, spendings)
    plt.show()