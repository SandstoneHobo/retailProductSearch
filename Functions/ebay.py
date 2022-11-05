from bs4 import BeautifulSoup as soup
import time
import requests

def connect(search, page):
  URL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + search + "&_sacat=0&LH_TitleDesc=0&_pgn=" + str(page)
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Upgrade-Insecure-Requests": "1"}

  page = requests.get(URL, headers=headers)
  return soup(page.content, "html.parser")

def Ebay(search):
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
    
    products = soup1.findAll("li",{"class":"s-item s-item__pl-on-bottom s-item--watch-at-corner"})
  
    for product in products:
      try:
        productName = product.div.div.next_sibling.a.div.text.strip()
        productPrice = product.find("div",{"class":"s-item__details clearfix"}).div.span.text
        productPrice = productPrice.replace(",", "")
        for i in range(0, len(productPrice)):
          if productPrice[i] == "$":
            productPrice = float(productPrice[i+1:i+6])
            break
        productLink = product.div.div.next_sibling.a["href"]

        newProduct = {"name":productName,"price":productPrice,"link":productLink}
        if(newProduct not in outputList and type(productPrice) is float):
          outputList.append(newProduct)
        else:
          pass
      except:
        pass
      
    count += 1
    time.sleep(5)
    
   

  return outputList
