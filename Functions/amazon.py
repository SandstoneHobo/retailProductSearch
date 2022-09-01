from bs4 import BeautifulSoup as soup
import time
import requests

def connect(search, pageNum):
  URL = "https://www.amazon.com/s?k=" + search + "&page=" + str(pageNum) + "&ref=nb_sb_noss"
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Upgrade-Insecure-Requests": "1"}
  
  page = requests.get(URL, headers=headers)

  return soup(page.content, "html.parser")


def Amazon(search):
  soup1 = connect(search, 1)
  outputList = []

  PageCount = int(soup1.find("div",{"class":"a-section a-text-center s-pagination-container"}).span.a.next_sibling.next_sibling.next_sibling.text)

  for page in range(1, PageCount + 1):
    if page != 1:
      soup1 = connect(search, page)

    products = soup1.findAll("div", {"class":"sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right"})
  

    for product in products:
      try:
        productName = product.div.div.div.h2.a.span.text
        productPrice = product.find("span", {"class":"a-price"}).text
        productPrice = productPrice.replace(",", "")
        productPrice = float(productPrice[1:7])
        productLink = "https://www.amazon.com" + product.div.div.div.next_sibling.next_sibling.div.div.div.div.a["href"]
        

        newProduct = {"name":productName,"price":productPrice,"link":productLink}
        outputList.append(newProduct)
      except:
        pass
    time.sleep(5)

  return outputList
