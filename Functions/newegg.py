from bs4 import BeautifulSoup as soup
import requests

def Newegg(search):
  URL = "https://www.newegg.com/p/pl?d=" + search
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Upgrade-Insecure-Requests": "1"}

  outputList = []

  page = requests.get(URL, headers=headers)

  soup1 = soup(page.content, "html.parser")

  products = soup1.findAll("div", {"class":"item-cell"})

  for product in products:
    try:
      productName = product.div.a.img["alt"]
      productPrice = product.find("div",{"class":"item-action"}).ul.find("li",{"class":"price-current"}).strong.text + product.find("div",{"class":"item-action"}).ul.find("li",{"class":"price-current"}).sup.text
      productPrice = productPrice.replace(",", "")
      productPrice = float(productPrice)
      productLink = product.div.a["href"]

      newProduct = {"name":productName,"price":productPrice,"link":productLink}
      outputList.append(newProduct)
    except:
      pass


  return outputList
