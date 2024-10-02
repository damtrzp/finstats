from typing import List
from main import Transaction
import csv
from io import open

def readINGhistory(filepath = "./history.csv") -> List[Transaction]:
    result : List[Transaction] = []
    with open(filepath, 'rt', encoding="Windows-1250") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            try:
                curTrans = Transaction(
                    transactionDateStr=row[0],
                    amount=float(row[8].replace(",", ".")),
                    counterparty=row[2]
                )
                result.append(curTrans)
            except (ValueError, IndexError):
                pass
    return result