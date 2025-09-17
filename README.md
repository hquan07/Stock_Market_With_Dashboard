# 📊 Mid_FunDS – Stock ETL & Dashboard Project

## 🚀 Introduction
**Mid_FunDS** is a project that builds an **ETL (Extract – Transform – Load) pipeline** for stock market data and provides an interactive dashboard for analysis.

- **Extract**: Load raw stock data from CSV (`all_stocks_5yr.csv`).  
- **Transform**: Clean the dataset and calculate financial indicators (SMA 20, SMA 50, Daily Return).  
- **Load**: Insert the processed data into MySQL (`stocksdb.daily_prices`).  
- **Dashboard**: Visualize and analyze data with **Streamlit** or **Plotly Dash**.  

---

## 🗂 Project Structure
```bash
Mid_FunDS/
│
├── dataset/
│   └── all_stocks_5yr.csv          # Raw dataset
│
├── initialize_database/
│   └── mysql_schema.sql            # SQL script to create database & tables
│
├── src/
│   ├── etl/
│   │   ├── extract.py              # Extract step
│   │   ├── transform.py            # Transform step
│   │   ├── load.py                 # Load step
│   │   └── run_etl.py              # Run the full ETL pipeline
│   │
│   ├── utils/
│   │   └── db.py                   # MySQL connection helper
│   │
│   └── dashboard/
│       ├── dashboard.py            # Streamlit dashboard
│       └── app.py                  # Plotly Dash dashboard
│
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## 🛠 Requirements
- **Python 3.10+**
- **MySQL 8.0+**
- Python libraries:
  ```bash
  pip install -r requirements.txt
  ```

`requirements.txt`:
```txt
pandas
numpy
sqlalchemy
mysql-connector-python
streamlit
dash
plotly
```

---

## 🗄 Database Setup
Use the provided SQL script to initialize the database schema:

```bash
mysql -u root -p < initialize_database/mysql_schema.sql
```

SQL content (simplified):
```sql
CREATE DATABASE stocksdb;
USE stocksdb;

CREATE TABLE IF NOT EXISTS daily_prices (
  id INT AUTO_INCREMENT PRIMARY KEY,
  symbol VARCHAR(16) NOT NULL,
  trade_date DATE NOT NULL,
  open DECIMAL(18,6),
  high DECIMAL(18,6),
  low DECIMAL(18,6),
  close DECIMAL(18,6),
  volume BIGINT,
  sma_20 DECIMAL(18,6),
  sma_50 DECIMAL(18,6),
  daily_return DECIMAL(18,6),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT uniq_symbol_date UNIQUE (symbol, trade_date)
);

CREATE INDEX idx_symbol_date ON daily_prices (symbol, trade_date);
```

---

## ⚙️ Running ETL
Run the pipeline to extract, transform, and load data into MySQL:

```bash
cd Mid_FunDS
python -m src.etl.run_etl
```

Steps:
- `[EXTRACT]` Load raw CSV file  
- `[TRANSFORM]` Clean data & compute SMA 20, SMA 50, Daily Return  
- `[LOAD]` Insert into MySQL  

---

## 📊 Running Dashboards

### 1. Streamlit
```bash
streamlit run src/dashboard/dashboard.py
```
Browser: [http://localhost:8501](http://localhost:8501)

### 2. Plotly Dash
```bash
python src/dashboard/app.py
```
Browser: [http://127.0.0.1:8050](http://127.0.0.1:8050)

---

## 📈 Features
- Interactive stock price charts  
- Compare SMA 20 and SMA 50  
- Analyze **Daily Return (%)**  
- Filter by symbol and time range  

---

## 📬 Contact
Email: huyquan1607@gmail.com

---
