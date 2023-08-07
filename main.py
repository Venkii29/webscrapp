import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
''''
page=requests.get("https://www.espncricinfo.com/series/indian-premier-league-2023-1345038/points-table-standings")
soup=BeautifulSoup(page.text,"html.parser")
table=soup.find("table")
team=[]
for i in table.find_all("span",class_ = "ds-text-tight-s ds-font-bold ds-uppercase ds-text-left ds-text-typo"):
    team.append(i.text)
match=[]
won=[]
for j in table.find_all("td",class_ = "ds-w-0 ds-whitespace-nowrap ds-min-w-max")[0::8]:
    match.append(j.text)
for k in table.find_all("td",class_ = "ds-w-0 ds-whitespace-nowrap ds-min-w-max")[1::8]:
    won.append(k.text)
loss=[]
for l in table.find_all("td",class_ = "ds-w-0 ds-whitespace-nowrap ds-min-w-max")[2::8]:
    loss.append(l.text)
tie=[]
for m in table.find_all("td",class_ = "ds-w-0 ds-whitespace-nowrap ds-min-w-max")[3::8]:
    tie.append(m.text)
run_rate=[]
for n in table.find_all("td",class_ = "ds-w-0 ds-whitespace-nowrap ds-min-w-max")[4::8]:
    run_rate.append(n.text)
df = pd.DataFrame({"TEAMS":team,"W":won})
print(df)'''


with open ("auction.json") as f:
    data=json.load(f)

df=pd.DataFrame(column=["TEAM","PLAYER","TYPE","PRICE"])
print(df)

