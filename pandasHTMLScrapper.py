import pandas as pd
'''
this could be really quick and useful where there is some table with html tags like <table> <tr> <td> etc
returns a list of DFs, even if there is only one table on the page
behind the scens it does use requests and bs4 like modules
could be really useful for wikipedia data tables
try to remember this method can be used for some table srapping quick and easy
also can give it some arguments like parse_date, skiprows; see docs
could as easily save into a csv file with to_csv
'''
pageDfList=pd.read_html('https://fastestlaps.com/tracks/le-mans-bugatti')

print(len(pageDfList))
if len(pageDfList)>0:
    df=pageDfList[0]
    print(df.shape)
    print(df.head())
    print(df.columns)

#df.to_csv('lapes-time.csv',index=False)