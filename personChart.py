import pdb
from typing import List
from main import Transaction, getTransactionsOfCounterparty, dateTickFormatter
import matplotlib.pyplot as plt
from matplotlib import ticker
import pandas as pd

def getIntervalsAndAmountsData(name : str, allTransactions : List[Transaction], minAmount : float = 0, maxAmount : float = 250):
    transactions = getTransactionsOfCounterparty(name, allTransactions)

    # Get the first date's timestamp and delete the first row from the list
    firstDateStr = transactions[0].transactionDateStr
    lastDate = transactions[0].transactionDateEpoch
    transactions.pop(0)

    intervals = []
    amounts = []

    # Make the graph
    fig, ax = plt.subplots()
    ax.set_xlabel("Time since last payment", rotation_mode="default")
    ax.set_ylabel("Payment amount")

    for row in transactions:
        amount = row.amount
        if amount > minAmount and amount < maxAmount:
            curDate = row.transactionDateEpoch
            interval = lastDate - curDate
            interval = interval / 60 / 60 / 24
            lastDate = curDate
            intervals.append(interval)
            amounts.append(amount)

    print("Pierwsza transakcja: ", firstDateStr)
    print("Ostatnia transakcja: ", transactions[-1].transactionDateStr)

    #print("opaltv: ",
    #      datetime.datetime.strptime(firstDateStr, "%Y-%m-%d").timestamp() - datetime.datetime.strptime(transactions[-1][0],
    # "%Y-%m-%d").timestamp())

    print("Suma: ", sum(amounts))

    # ax.bar(intervals, amounts)
    # plt.hist(intervals, amounts, bins=10)
    df = pd.DataFrame({
        'Interval': intervals,
        'Amount': amounts
    })

    print(intervals)
    print("Average: of intervals: ", sum(intervals) / len(intervals))
    print("Standard deviation of intervals: ", df["Interval"].std())

    # df.groupby("Interval")["Amount"].plot(kind="hist",edgecolor='black')
    # df.plot(x="Interval", y="Amount")
    # plt.hist2d(x=df.loc[:,"Interval"], y=df.loc[:,"Amount"])
    plt.scatter(x=df["Interval"], y=df["Amount"])
    plt.show()

def transactionsByTimePlot(name : str, allTransactions : List[Transaction], minAmount : float = -100, maxAmount : float = 250):
    transactions = getTransactionsOfCounterparty(name, allTransactions)
    times = []
    amounts = []

    for transaction in transactions:
        amount = transaction.amount
        print("Amount: ", amount)
        if amount > minAmount and amount < maxAmount:
            times.append(transaction.transactionDateEpoch)
            amounts.append(transaction.amount)
    df = pd.DataFrame({
        "Date": times,
        "Amount": amounts
    })

    ax = plt.axes()
    ax.scatter(x=df["Date"], y=df["Amount"])



    fmt = ticker.FuncFormatter(dateTickFormatter)
    ax.xaxis.set_major_formatter(fmt)
    print("Times from DF: ", times)
    plt.show()