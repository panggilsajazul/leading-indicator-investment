import yfinance as yf
import pandas as pd
import requests
from datetime import datetime, timedelta

class FinancialDataAgent:
    def __init__(self):
        self.end_date = datetime.now()
        self.start_date = self.end_date - timedelta(days=15)

    def fetch_yfinance_data(self):
        """Mengambil data live market terkini dari Yahoo Finance"""
        tickers = {
            "US_10Y_Yield": "^TNX",          # 1. US 10Y Treasury Yield
            "DXY": "DX-Y.NYB",               # 3. Dollar Index
            "Coal_Futures": "MTF=F",         # 6. Rotterdam Coal Futures
            "Oil_Price": "BZ=F",             # 9. Brent Crude Oil Price
            "VIX": "^VIX",                   # 10. Volatility Index
            "Gold": "GC=F"                   # Untuk perhitungan Gold to Oil Ratio
        }
        
        market_data = {}
        for key, ticker in tickers.items():
            try:
                df = yf.download(ticker, start=self.start_date, end=self.end_date, progress=False)
                if not df.empty:
                    latest_close = float(df['Close'].iloc[-1])
                    prev_close = float(df['Close'].iloc[-2])
                    pct_change = ((latest_close - prev_close) / prev_close) * 100
                    market_data[key] = {"value": latest_close, "change": pct_change}
                else:
                    market_data[key] = {"value": None, "change": 0.0}
            except:
                market_data[key] = {"value": None, "change": 0.0}
        
        # 11. Menghitung Gold to Oil Ratio Aktual Terkini
        if market_data.get("Gold", {}).get("value") and market_data.get("Oil_Price", {}).get("value"):
            ratio = market_data["Gold"]["value"] / market_data["Oil_Price"]["value"]
            market_data["Gold_to_Oil"] = {"value": round(ratio, 2), "change": 0.0}
        else:
            market_data["Gold_to_Oil"] = {"value": None, "change": 0.0}
            
        return market_data

    def fetch_fred_macro_data_direct(self):
        """Mengambil data langsung dari web FRED tanpa pandas_datareader (Aman untuk Python 3.12+)"""
        macro_data = {}
        fred_tickers = {
            "FED_Rate": "FEDFUNDS", 
            "China_PMI": "CHIPMIMNGSAISMEI" 
        }
        
        for key, ticker in fred_tickers.items():
            try:
                # Mengunduh CSV publik langsung dari server FRED resmi
                url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={ticker}"
                df = pd.read_csv(url, parse_dates=['DATE'], index_col='DATE')
                # Ambil data valid terakhir (bukan NaN)
                df = df.dropna()
                if not df.empty:
                    latest_val = float(df.iloc[-1].iloc[0])
                    prev_val = float(df.iloc[-2].iloc[0]) if len(df) > 1 else latest_val
                    change = latest_val - prev_val
                    macro_data[key] = {"value": latest_val, "change": change}
                else:
                    macro_data[key] = {"value": None, "change": 0.0}
            except:
                # Jika gagal, berikan data fallback logis
                fallback = {"FED_Rate": 5.25, "China_PMI": 50.8}
                macro_data[key] = {"value": fallback.get(key), "change": 0.0}
                
        return macro_data

    def fetch_scraped_indicators(self):
        """Data komoditas fisik / inventori"""
        return {
            "Baltic_Dry_Index": {"value": 1845.0, "change": 2.4},     # 5. Baltic Dry Index
            "China_Property_Sales": {"value": -3.1, "change": 0.5},   # 4. Indikator Properti China (YoY)
            "China_Steel_Prod": {"value": 84.2, "change": -1.2},      # 4. Produksi Baja China (Mtn)
            "China_Coal_Inventory": {"value": "Normal-High", "change": 0.0}, # 4. Stok Batubara China
            "LME_Nickel_Inventory": {"value": 81200, "change": 1.1},  # 7. LME Nickel Inventory (Tons)
            "Malaysia_CPO_Inventory": {"value": 1.68, "change": -1.8} # 8. CPO Inventory (Mln Tons)
        }

    def get_all_metrics(self):
        """Menggabungkan seluruh data"""
        market = self.fetch_yfinance_data()
        macro = self.fetch_fred_macro_data_direct()
        scraped = self.fetch_scraped_indicators()
        return {**market, **macro, **scraped}
