wget --quiet \
  --method POST \
  --header 'cookie: AWSELB=E7D97B4314FA26C81AC086FF58630988BE484265E5374D256569558AF614CC99D266B72FDD595D0A0485F1CEF3237F07E8299A0DF7B22B0E292E8C4257E382CEDA0A3BCACF; AWSELBCORS=E7D97B4314FA26C81AC086FF58630988BE484265E5374D256569558AF614CC99D266B72FDD595D0A0485F1CEF3237F07E8299A0DF7B22B0E292E8C4257E382CEDA0A3BCACF' \
  --header 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0' \
  --header 'Accept: */*' \
  --header 'Accept-Language: en-US,en;q=0.5' \
  --header 'Referer: https://www.fihproleague.com/' \
  --header 'Content-Type: application/json' \
  --header 'Origin: https://www.fihproleague.com' \
  --header 'Connection: keep-alive' \
  --header 'Sec-Fetch-Dest: empty' \
  --header 'Sec-Fetch-Mode: cors' \
  --header 'Sec-Fetch-Site: cross-site' \
  --body-data '{"perPage":"200","page":1,"competition_id":1295,"team_id":[],"venus_id":[]}' \
  --output-document \
  - https://www.worldcup2018.hockey/admin/api/v1/matches/get-match-statics-list

# copied code from insomania applicatoin request