import requests
fmp_api_key=""
def get_earnings(api_key):
    print("fetching data..")
    url=f"https://financialmodelingprep.com/api/v3/earning_calendar?apikey={api_key}&limit=5"
    response=requests.get(url)
    print(response.status_code)
    if response.status_code== 200:
        return response.json()
    else:
        print("somethng exploded")
        return []

earnings=get_earnings(fmp_api_key)

for company in earnings:
    print(f"{company['date']}: {company['company']} ({company['symbol']})")
