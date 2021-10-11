import gspread

def gSheet(productList):
    googleCreds=gspread.service_account(filename='googleSheetsCreds.json')
    googleSheet=googleCreds.open('yellPagesUK').sheet1
    googleSheet.append_row(str(productList['name']),str(productList['category']),str(productList['meta']),str(productList['website']))
    return None