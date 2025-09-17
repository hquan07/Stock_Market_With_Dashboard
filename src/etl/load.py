from mysql.connector import Error
from src.utils.db import get_connection

def load(df):
    """
    Load transformed stock data into MySQL table daily_prices
    """
    print("[LOAD] Inserting into MySQL...")

    try:
        conn = get_connection()
        if conn is None:
            print("❌ No database connection")
            return

        cursor = conn.cursor()

        insert_query = """
            INSERT INTO daily_prices 
            (symbol, trade_date, open, high, low, close, volume, sma_20, sma_50, daily_return)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        for row in df.itertuples(index=False):
            cursor.execute(insert_query, (
                row.Name,                          # symbol
                row.date.date(),                   # convert pandas.Timestamp -> datetime.date
                float(row.open),
                float(row.high),
                float(row.low),
                float(row.close),
                int(row.volume),
                float(row.sma_20),
                float(row.sma_50),
                float(row.daily_return)
            ))

        conn.commit()
        print(f"✅ Loaded {len(df)} rows into daily_prices")

    except Error as e:
        print("❌ MySQL load error:", e)

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("🔌 MySQL connection closed")
