import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    print("[TRANSFORM] Cleaning and calculating indicators...")

    df["date"] = pd.to_datetime(df["date"])

    df = df.sort_values(by=["Name", "date"])

    df["sma_20"] = df.groupby("Name")["close"].transform(lambda x: x.rolling(20).mean())
    df["sma_50"] = df.groupby("Name")["close"].transform(lambda x: x.rolling(50).mean())
    df["daily_return"] = df.groupby("Name")["close"].transform(lambda x: x.pct_change())

    df = df.dropna().reset_index(drop=True)

    print(f"[TRANSFORM] After cleaning: {len(df)} rows")
    return df
