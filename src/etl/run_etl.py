from src.etl.extract import extract
from src.etl.transform import transform
from src.etl.load import load

def run_etl():
    filepath = "C:\\Mid_FunDS\\dataset\\all_stocks_5yr.csv"

    df = extract(filepath)
    df = transform(df)
    load(df)

if __name__ == "__main__":
    run_etl()
