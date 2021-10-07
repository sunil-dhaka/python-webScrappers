import requests

url = "https://www.worldcup2018.hockey/admin/api/v1/matches/get-match-statics-list"

payload = {
    "perPage": "200",
    "page": 1,
    "competition_id": 1295,
    "team_id": [],
    "venus_id": []
}
headers = {
    "cookie": "AWSELB=E7D97B4314FA26C81AC086FF58630988BE484265E5374D256569558AF614CC99D266B72FDD595D0A0485F1CEF3237F07E8299A0DF7B22B0E292E8C4257E382CEDA0A3BCACF; AWSELBCORS=E7D97B4314FA26C81AC086FF58630988BE484265E5374D256569558AF614CC99D266B72FDD595D0A0485F1CEF3237F07E8299A0DF7B22B0E292E8C4257E382CEDA0A3BCACF",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.fihproleague.com/",
    "Content-Type": "application/json",
    "Origin": "https://www.fihproleague.com",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)

# copied code from insomania applicatoin request