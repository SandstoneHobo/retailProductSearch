from bs4 import BeautifulSoup as soup
import time
import requests

def connect(search, page):
  URL = "https://www.bestbuy.com/site/searchpage.jsp?cp=" + str(page) + "&id=pcat17071&st=" + search
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Upgrade-Insecure-Requests": "1"}

  page = requests.get(URL, headers=headers)

  return soup(page.content, "html.parser")

  
def BestBuy(search):
  soup1 = connect(search, 1)
  outputList = []
  pages = True
  count = 1

  while(pages):
    if count != 1 and count <= 10:
      soup1 = connect(search, count)
      print("\n Getting results for page: " + str(count))
    elif count == 1:
      print("\n Getting results for page: " + str(count))
    else:
      break

    products = soup1.findAll("li", {"class":"sku-item"})
    
    for product in products:
      try:
        productName = product.div.div.div.div.div.div.h4.a.text
        productPrice = product.div.div.div.div.div.div.next_sibling.div.div.div.div.div.div.div.div.div.div.div.span.text
        productPrice = productPrice.replace(",", "")
        productPrice = float(productPrice[1:])
        productLink = product.div.div.div.div.div.a["href"]
        productLink = "https://bestbuy.com" + productLink

        newProduct = {"name":productName,"price":productPrice,"link":productLink}
        outputList.append(newProduct)
      except:
        pass
      
    count += 1

  return outputList


