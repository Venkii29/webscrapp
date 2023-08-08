import json
import pandas as pd
with open("iplauction.json") as file:
    data=json.load(file)
    df=pd.DataFrame(columns=["TEAM","PLAYER","TYPE","PRICE"])
    for i in range(0,len(data)):
        df.loc[i]=[data[i]["TEAM"],data[i]["PLAYER"],data[i]["TYPE "],data[i]["PRICE"]]
    print(df)