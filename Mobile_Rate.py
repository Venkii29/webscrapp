import pandas
import requests
from bs4 import BeautifulSoup
names=[]
prices=[]
desc=[]
for i in range(1,21):
    page=requests.get("https://www.flipkart.com/search?q=mobiles%20phones%20under%2040000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"+"&page="+str(i))
    soup=BeautifulSoup(page.text,"html.parser")
    sec=soup.find("div",class_="_1YokD2 _3Mn1Gg")
    for i in sec.find_all("div", class_="_4rR01T"):
        names.append(i.text)
    for j in sec.find_all("div",class_ = "_30jeq3 _1_WHN1"):
        prices.append(j.text)
    for k in sec.find_all("div",class_ = "fMghEO"):
        desc.append(k.text)
df = pandas.DataFrame({"product_names":names,"product_prices":prices,"description":desc})
print(df)

