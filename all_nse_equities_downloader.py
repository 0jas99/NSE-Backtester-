import pandas as pd
import requests

def save_csv(name, symbols):
    df = pd.DataFrame({'Symbol': symbols})
    df.to_csv(name, index=False)
    print(f"✅ Saved {name} with {len(symbols)} symbols.")

def fetch_nifty_symbols(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        raise Exception("❌ Failed to fetch data from NSE.")
    dfs = pd.read_html(r.text)
    df = dfs[0]
    return df['Symbol'].str.strip().tolist()

if __name__ == "__main__":
    print("📥 Fetching NIFTY index constituent symbols...")

    try:
        nifty50_url = "https://www1.nseindia.com/content/indices/ind_nifty50list.csv"
        midcap100_url = "https://www1.nseindia.com/content/indices/ind_niftymidcap100list.csv"
        smallcap100_url = "https://www1.nseindia.com/content/indices/ind_niftysmallcap100list.csv"

        nifty50 = fetch_nifty_symbols(nifty50_url)
        midcap100 = fetch_nifty_symbols(midcap100_url)
        smallcap100 = fetch_nifty_symbols(smallcap100_url)

        # Append ".NS" for Yahoo Finance
        nifty50 = [s + ".NS" for s in nifty50]
        midcap100 = [s + ".NS" for s in midcap100]
        smallcap100 = [s + ".NS" for s in smallcap100]

        save_csv("nifty50_symbols.csv", nifty50)
        save_csv("nifty_midcap100_symbols.csv", midcap100)
        save_csv("nifty_smallcap100_symbols.csv", smallcap100)

        print("🎉 All CSVs saved successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")
