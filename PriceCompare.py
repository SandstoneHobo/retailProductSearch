#import libraries
import time
import datetime
import csv
from Functions import ebay as eba
from Functions import amazon as ama
from Functions import newegg as new
from Functions import walmart as wal
from Functions import bestbuy as bes
from Functions import dbController as database

def filterResults(results):
    resultList = []
    flag = True
    for i in range(len(results)):
        for j in range(len(results)):
            if(results[i]["link"] == results[j]["link"] and i != j):
                flag = False
        if(flag):
            resultList.append(results[i])

        flag = True

    return resultList

#takes in user input and replaces any spaces with + so that it can be used in a URL
search = str(input("What do you want the price of?: "))
search = search.replace(" ", "+")

#runs all the functions to gather results while printing its current progress
print("Getting results from Walmart....")
walmartResultList = wal.Walmart(search)
print("\n Finished with Walmart results \n")
print("Getting results from Amazon....")
amazonResultList = ama.Amazon(search)
print("\n Finished with Amazon results \n")
print("Getting results from BestBuy....")
bestbuyResultList = bes.BestBuy(search)
print("\n Finished with BestBuy results \n")
print("Getting results from NewEgg....")
neweggResultList = new.Newegg(search)
print("\n Finished with NewEgg results \n")
print("Getting results from Ebay....")
ebayResultList = eba.Ebay(search)
print("\n Finished with Ebay results \n")


#sums up all the lists that were returned and then sorts them by price each item in the list is a dictionary containing the name, price, and link to the product
combinedResultList = walmartResultList + amazonResultList + bestbuyResultList + neweggResultList + ebayResultList
finalResultList = sorted(combinedResultList, key=lambda x: x["price"])

#gets the current date and creates the result file with the date and search so it is clear what and when you searched
today = datetime.date.today()
fileName = "Results/" + search + str(today) + ".csv"

#opens the file as f to write in the data
with open(fileName, "w", newline='',encoding='UTF8') as f:
  #creates a header for the csv file with name, price, and link of the product
  csvHeader = ["Name", "Price", "Link"]

  #creates a writer variable to use the writing function of the csv module
  writer = csv.writer(f)
  #adds the header to the csv file
  writer.writerow(csvHeader)

  #loops through our list of product results
  for result in finalResultList:
    #creates a list of the values from this dictionary in our list of products
    valList = list(result.values())
    #Writes this list of values to the csv file
    writer.writerow(valList)
