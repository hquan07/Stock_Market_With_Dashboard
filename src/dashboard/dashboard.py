import streamlit as st
import pandas as pd
import plotly.express as px
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname('C:\Mid_FunDS\src\dashboard\dashboard.py'), "..")))
from utils.db import get_connection

# -----------------------------------------------------------------------------
# Load data from MySQL
# -----------------------------------------------------------------------------
def load_data():
    try:
        conn = get_connection()
        if conn is None:
            return pd.DataFrame()
        query = """
            SELECT symbol, trade_date, open, high, low, close, volume, sma_20, sma_50, daily_return
            FROM daily_prices
            ORDER BY trade_date
        """
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Error as e:
        st.error(f"MySQL error: {e}")
        return pd.DataFrame()

# -----------------------------------------------------------------------------
# Streamlit UI
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Stock Dashboard", layout="wide")
st.title("📊 Stock Data Dashboard")

df = load_data()

if df.empty:
    st.warning("⚠️ No data found in database. Please run ETL first.")
else:
    st.write("✅ Data loaded successfully")
    st.write("Preview:", df.head())

    # Sidebar
    company = st.sidebar.selectbox("Select company", sorted(df["symbol"].unique()))

    # Filter data
    dff = df[df["symbol"] == company]

    # Closing Price chart with SMA
    fig1 = px.line(dff, x="trade_date", y="close", title=f"{company} Closing Price")
    fig1.add_scatter(x=dff["trade_date"], y=dff["sma_20"], mode="lines", name="SMA 20", line=dict(color="orange"))
    fig1.add_scatter(x=dff["trade_date"], y=dff["sma_50"], mode="lines", name="SMA 50", line=dict(color="green"))
    st.plotly_chart(fig1, use_container_width=True)

    # Volume chart
    fig2 = px.bar(dff, x="trade_date", y="volume", title=f"{company} Trading Volume")
    st.plotly_chart(fig2, use_container_width=True)

    # Daily return chart
    fig3 = px.line(dff, x="trade_date", y="daily_return", title=f"{company} Daily Returns")
    st.plotly_chart(fig3, use_container_width=True)


