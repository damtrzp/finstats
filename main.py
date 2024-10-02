import math
import pdb
import time
import datetime
from typing import List
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import ticker

font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 6}

mpl.rc('font', **font)


class Transaction:
    transactionDateStr : str
    transactionDateEpoch : float
    amount : float
    counterparty : str

    def __init__(self, transactionDateStr : str, amount : float, counterparty : str):
        self.counterparty = counterparty
        self.amount = amount
        self.transactionDateStr = transactionDateStr
        self.transactionDateEpoch = datetime.datetime.strptime(transactionDateStr, "%Y-%m-%d").timestamp()
    def __str__(self):
        return f'[{self.transactionDateStr}, {self.counterparty}, {self.amount}]'
    def __repr__(self):
        return f'[{self.transactionDateStr}, {self.counterparty}, {self.amount}]'

def getTransactionsOfCounterparty(counterpartyName : str, allTransactions : List[Transaction]):
    transactions = []
    for curTransaction in allTransactions:
        if counterpartyName in curTransaction.counterparty:
            transactions.append(curTransaction)
    return transactions

def dateTickFormatter(x, pos):
    return datetime.datetime.fromtimestamp(x).strftime('%m-%d')
def cutoffStringArr(arr, maxLen = 10):
    result = []
    for i in range(len(arr)):
        result.append(arr[i][0:maxLen] + "...")
    return result

def dictToBarChart(dict):

    xAxis = list(dict.keys())
    xAxis = cutoffStringArr(xAxis)
    plt.figure(figsize=(
        len(xAxis),
        len(xAxis) / 3
    ))
    plt.style.use("ggplot")
    plt.bar(xAxis, dict.values())

    plt.show()


def getDayOfWeekFromEpoch(epoch : float):
    # Calculate the number of days since 1970-01-01 minus 3 days (To change the epoch start from Thursday to Monday)
    days = math.floor( (epoch + 259200) / 60 / 60 / 24)
    dayOfWeek = days % 7
    return dayOfWeek
