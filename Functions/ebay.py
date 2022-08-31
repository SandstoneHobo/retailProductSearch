from bs4 import BeautifulSoup as soup
import requests

def Ebay(search):
  URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=" + search + "&_sacat=0&LH_TitleDesc=0&_odkw="+ search + "&_osacat=0"
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Upgrade-Insecure-Requests": "1"}

  outputList = []

  page = requests.get(URL, headers=headers)
  soup1 = soup(page.content, "html.parser")

  products = soup1.findAll("li",{"class":"s-item s-item__pl-on-bottom s-item--watch-at-corner"})

  for product in products:
    try:
      productName = product.div.div.next_sibling.a.h3.text.strip()
      productPrice = product.find("div",{"class":"s-item__details clearfix"}).div.span.text
      productPrice = productPrice.replace(",", "")
      productPrice = float(productPrice[1:])
      productLink = product.div.div.next_sibling.a["href"]

      newProduct = {"name":productName,"price":productPrice,"link":productLink}
      outputList.append(newProduct)
    except:
      pass
      

  return outputList
