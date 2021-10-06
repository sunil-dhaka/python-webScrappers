import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
# skysports has easy scrapping table
link='https://www.skysports.com/premier-league-table'
r=requests.get(link)
print('Status for link : ',r.status_code)

leagueSoup=bs(r.text,features='html.parser')

tableData=leagueSoup.find('table',class_='standing-table__table callfn').find_all('tbody')
totalLen=len(tableData)

rawData=list()
for i in range(totalLen):
    for row in tableData[i].find_all('tr',class_='standing-table__row'):
        cells=row.find_all('td',class_='standing-table__cell')
        team={
            'name':row.a.text,
            'played':int(cells[2].text),
            'points':int(cells[9].text)
        }
        rawData.append(team)

print('total teams in standing table',len(rawData))

leagueDF=pd.DataFrame(rawData)

print(leagueDF.shape)

# store in csv or whatever 
#leagueDF.to_csv('league-data.csv',index=False)
#leagueDF.to_excel('league-data.xlsx')