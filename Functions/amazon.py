from bs4 import BeautifulSoup as soup
import time
import requests

#helper function to create a connection to amazon takes in a search term and page number to connect to
def connect(search, pageNum):
  #creates variables to hold the link built from the seatch term and page number, as well as one to hold the browser headers to convince them you are not a bot
  URL = "https://www.amazon.com/s?k=" + search + "&page=" + str(pageNum) + "&ref=nb_sb_noss"
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Upgrade-Insecure-Requests": "1"}

  #creates a variable to store the page we retrieve and then return the raw html of the page using beautiful soup module
  page = requests.get(URL, headers=headers)

  return soup(page.content, "html.parser")

#the amazon function that goes through each page and gets the product info
def Amazon(search):
  #stores the raw html gained from the helper function and a list to hold all of the dictionaries holding product information
  soup1 = connect(search, 1)
  outputList = []

  #loops 10 times to go through the first 10 pages of results from amazon
  for page in range(1, 11):
    #if this is not the first page, we create a new connection to the page we need to be on and prints which page we are currently gathering
    if page != 1:
      soup1 = connect(search, page)
      print("\n Getting results for page: " + str(page))
    else:
      #prints that we are getting page 1 results
      print("\n Getting results for page: 1")

    #uses beautiful soup to find all the products by searching for any element with a specific div tag and makes a list of them
    products = soup1.findAll("div", {"class":"sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right"})
  
    #loops through the the list of products found through the tag
    for product in products:
      #trys to get the product inforation by going to sub html tags
      try:
        productName = product.div.div.div.h2.a.span.text
        productPrice = product.find("span", {"class":"a-price"}).text
        #replaces commas in the price with empty strings so that it can be converted to a float
        productPrice = productPrice.replace(",", "")
        #loops through the price string to remove the dollar sign so it can be converted to a float
        for i in range(0, len(productPrice)):
          if productPrice[i] == "$":
            productPrice = float(productPrice[i+1:i+6])
            #breaks the loop after the dollar sign is removed
            break
        productLink = "https://www.amazon.com" + product.div.div.div.next_sibling.next_sibling.div.div.div.div.a["href"]
        
        #creates a dictionary with all the info and appends it to the output
        newProduct = {"name":productName,"price":productPrice,"link":productLink}
        if(newProduct not in outputList and type(productPrice) is float):
          outputList.append(newProduct)
        else:
          pass
      except:
        #if there were errors getting a products info, we will skip that product
        pass
    #sleeps for 5 seconds to avoid getting timed out by the website
    time.sleep(5)

  return outputList
