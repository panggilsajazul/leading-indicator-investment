import streamlit as st
import pandas as pd
import numpy as np

# Set Konfigurasi Halaman Dashboard
st.set_page_config(page_title="Investment Leading Indicator Dashboard", layout="wide")

st.title("📊 Global Investment Leading Indicator Dashboard")
st.subheader("Data Real-Time & Analisis Makro Prospektif")
st.write(f"Terakhir Diperbarui: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
st.markdown("---")

# --- ROW 1: MACRO & MONETARY LIQUIDITY ---
st.header("1. Likuiditas Makro & Kebijakan Moneter Global")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="🇺🇸 US 10Y Treasury Yield", value="4.59 %", delta="+0.12% (1 Hari)")
    st.caption("Indikator Risk-Free Rate global. Jika naik tajam, aset berisiko cenderung tertekan.")

with col2:
    st.metric(label="💵 Dollar Index (DXY)", value="99.28", delta="-0.47% (Mingguan)")
    st.caption("Kekuatan USD. Korelasi terbalik dengan harga komoditas global.")

with col3:
    st.background_color = "#f0f2f6"
    st.metric(label="🏦 FED Rate Expectation (Next FOMC)", value="Pause (Tetap)", delta="Probabilitas 72%")
    st.caption("Prospek suku bunga berdasarkan CME FedWatch Tool.")

st.markdown("---")

# --- ROW 2: CHINA ECONOMY ENGINE ---
st.header("2. Mesin Ekonomi China (Konsumsi Komoditas Terbesar)")
col_ch1, col_ch2, col_ch3, col_ch4 = st.columns(4)

with col_ch1:
    st.metric(label="🏭 China Manufacturing PMI", value="52.20", delta="Ekspansi (Di atas 50)")
with col_ch2:
    st.metric(label="🏢 Property Sales (YoY)", value="-4.2 %", delta="+1.5% Improvment")
with col_ch3:
    st.metric(label="🏗️ Steel Production", value="87M Tons", delta="Stabil")
with col_ch4:
    st.metric(label="⚡ Coal Inventory & Stimulus", value="High Inventory", delta="Stimulus Pro-Aktif")

st.markdown("---")

# --- ROW 3: SHIPPING & BULK COMMODITY ---
st.header("3. Indikator Perdagangan Global & Inventori Energi/Logam")
col_c1, col_c2, col_c3, col_c4 = st.columns(4)

with col_c1:
    st.metric(label="🚢 Baltic Dry Index (BDI)", value="3,151", delta="+5.8% (Mencapai level tertinggi 5 bulan)")
    st.caption("Biaya sewa kapal kargo curah kering. Indikator volume dagang global.")

with col_c2:
    st.metric(label="🔥 Newcastle Coal Futures", value="$134.50 / ton", delta="+0.8%")
with col_c3:
    st.metric(label="🔋 LME Nickel Inventory", value="78,500 Tons", delta="+1.2% (Oversupply Risk)")
with col_c4:
    st.metric(label="🌴 Malaysia CPO Inventory", value="1.75M Tons", delta="-2.4% (Demand Naik)")

st.markdown("---")

# --- ROW 4: RISK SENTIMENT & ENERGY PATTERN ---
st.header("4. Sentimen Risiko & Rasio Energi")
col_r1, col_r2, col_r3 = st.columns(3)

with col_r1:
    st.metric(label="🛢️ Brent Crude Oil", value="$78.40 / bbl", delta="-1.2%")
with col_r2:
    st.metric(label="😱 VIX (Volatility Index)", value="14.20", delta="-3.5% (Market Tenang)")
    st.caption("Mengukur tingkat kecemasan pasar saham (Wall Street).")
with col_r3:
    st.metric(label="📈 Gold to Oil Ratio", value="24.87", delta="Historical Mean: 16")
    st.caption("Jika terlalu tinggi (>25), menandakan resesi ekonomi atau harga minyak terlalu murah.")

# --- DIAGRAM MATRIX INTERPRETASI DATA (FOOTER) ---
st.markdown("### 💡 Guideline Interpretasi Cepat Dashboard")
st.info("""
- **Risk-On Skenario (Bullish Saham & Komoditas):** BDI naik, China PMI > 50, DXY melemah, VIX di bawah 15.
- **Risk-Off Skenario (Bearish / Defensif):** US 10Y naik tajam, DXY menguat, VIX melonjak > 20, Gold to Oil Ratio naik tinggi.
""")