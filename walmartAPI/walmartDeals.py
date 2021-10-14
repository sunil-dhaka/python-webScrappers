import pandas as pd
import json

with open('walmart.json','r') as f:
    data=json.load(f)

productData=data['data']['search']['searchResult']

print(productData['aggregatedCount'])

items=productData['itemStacks'][0]['itemsV2']

itemList=list()
for item in items:
    try:
        itemData={
            'name':item['name'],
            'price':item['priceInfo']['currentPrice']['price'],
            'url':'https://www.walmart.com'+item['canonicalUrl'],
            'image':item['imageInfo']['thumbnailUrl']
        }
        itemList.append(itemData)
    except:
        pass

itemsDF=pd.DataFrame(itemList)

itemsDF.to_csv('walmart.csv',index=False)