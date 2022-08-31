#import libraries
import time
import datetime
import csv
from Functions import ebay as eba
from Functions import amazon as ama
from Functions import newegg as new
from Functions import walmart as wal
from Functions import bestbuy as bes

search = str(input("What do you want the price of?: "))
search = search.replace(" ", "+")

walmartResultList = wal.Walmart(search)
amazonResultList = ama.Amazon(search)
bestbuyResultList = bes.BestBuy(search)
neweggResultList = new.Newegg(search)
ebayResultList = eba.Ebay(search)

combinedResultList = walmartResultList + amazonResultList + bestbuyResultList + neweggResultList + ebayResultList
finalResultList = sorted(combinedResultList, key=lambda x: x["price"])

today = datetime.date.today()
fileName = "Results/" + search + str(today) + ".csv"

with open(fileName, "w", newline='',encoding='UTF8') as f:
  csvHeader = ["Name", "Price", "Link"]
  
  writer = csv.writer(f)
  writer.writerow(csvHeader)
  
  for result in finalResultList:
    valList = list(result.values())

    writer.writerow(valList)
