import pandas as pd

def extract(filepath: str) -> pd.DataFrame:
    print(f"[EXTRACT] Reading data from {'C:\\Mid_FunDS\\dataset\\all_stocks_5yr.csv'}")
    df = pd.read_csv('C:\\Mid_FunDS\\dataset\\all_stocks_5yr.csv')

    print(f"[EXTRACT] Loaded {len(df)} rows, columns: {df.columns.tolist()}")
    return df
