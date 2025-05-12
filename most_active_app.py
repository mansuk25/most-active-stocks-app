import streamlit as st
import requests
import os
from dotenv import load_dotenv

# load environment variables from .env
load_dotenv()


# Retrive API key
FMP_API_KEY = os.getenv("FMP_API_KEY")

# Function to get most active stocks
def get_most_active_stocks(api_key):
    url = f"https://financialmodelingprep.com/api/v3/actives?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("API call failed. Check your key or the endpoint.")
        return []

# Streamlit UI starts here
st.set_page_config(page_title="Most Active Stocks", layout="centered")
st.title("📈 Most Active Stocks Today")

stocks = get_most_active_stocks(FMP_API_KEY)

if stocks:
    for stock in stocks[:10]:  # Show top 10
        st.subheader(f"{stock['ticker']} - {stock['companyName']}")
        st.write(f"**Price**: ${stock['price']}")
        st.write(f"**Change**: {stock['changesPercentage']}")
        st.markdown("---")
else:
    st.warning("No data to display.")