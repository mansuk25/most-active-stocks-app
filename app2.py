import requests 
fmp_api_key = "" # Replace with your real API key 
def get_most_active_stocks(api_key): 
    print("Fetching most active stocks...") 
    url = f"https://financialmodelingprep.com/api/v3/actives?apikey={api_key}" 
    response = requests.get(url) 
    print("Status code:", response.status_code) 
    if response.status_code == 200: 
        return response.json() 
    else: print("Something tragic occurred.") 
    return [] 
stocks = get_most_active_stocks(fmp_api_key) # Display basic info for each stock 
for stock in stocks[:10]: # limiting to first 10 for your fragile attention span 
    print(f"{stock['ticker']}: {stock['companyName']} | Price: ${stock['price']} | Change: {stock['changesPercentage']}")
