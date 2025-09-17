# \# 📊 Stock ETL \& Dashboard Project

# 

# \## 🚀 Introduction

# \*\*Stock ETL \& Dashboard Project\*\* is a project that builds an \*\*ETL (Extract – Transform – Load) pipeline\*\* for stock market data and provides an interactive dashboard for analysis.

# 

# \- \*\*Extract\*\*: Load raw stock data from CSV (`all\_stocks\_5yr.csv`).  

# \- \*\*Transform\*\*: Clean the dataset and calculate financial indicators (SMA 20, SMA 50, Daily Return).  

# \- \*\*Load\*\*: Insert the processed data into MySQL (`stocksdb.daily\_prices`).  

# \- \*\*Dashboard\*\*: Visualize and analyze data with \*\*Streamlit\*\* or \*\*Plotly Dash\*\*.  

# 

# ---

# 

# \## 🗂 Project Structure

# ```bash

# Mid\_FunDS/

# │

# ├── dataset/

# │   └── all\_stocks\_5yr.csv          # Raw dataset

# │

# ├── initialize\_database/

# │   └── mysql\_schema.sql            # SQL script to create database \& tables

# │

# ├── src/

# │   ├── etl/

# │   │   ├── extract.py              # Extract step

# │   │   ├── transform.py            # Transform step

# │   │   ├── load.py                 # Load step

# │   │   └── run\_etl.py              # Run the full ETL pipeline

# │   │

# │   ├── utils/

# │   │   └── db.py                   # MySQL connection helper

# │   │

# │   └── dashboard/

# │       ├── dashboard.py            # Streamlit dashboard

# │       └── app.py                  # Plotly Dash dashboard

# │

# ├── requirements.txt                # Python dependencies

# └── README.md                       # Project documentation

# ```

# 

# ---

# 

# \## 🛠 Requirements

# \- \*\*Python 3.10+\*\*

# \- \*\*MySQL 8.0+\*\*

# \- Python libraries:

# &nbsp; ```bash

# &nbsp; pip install -r requirements.txt

# &nbsp; ```

# 

# `requirements.txt`:

# ```txt

# pandas

# numpy

# sqlalchemy

# mysql-connector-python

# streamlit

# dash

# plotly

# ```

# 

# ---

# 

# \## 🗄 Database Setup

# Use the provided SQL script to initialize the database schema:

# 

# ```bash

# mysql -u root -p < initialize\_database/mysql\_schema.sql

# ```

# 

# SQL content (simplified):

# ```sql

# CREATE DATABASE stocksdb;

# USE stocksdb;

# 

# CREATE TABLE IF NOT EXISTS daily\_prices (

# &nbsp; id INT AUTO\_INCREMENT PRIMARY KEY,

# &nbsp; symbol VARCHAR(16) NOT NULL,

# &nbsp; trade\_date DATE NOT NULL,

# &nbsp; open DECIMAL(18,6),

# &nbsp; high DECIMAL(18,6),

# &nbsp; low DECIMAL(18,6),

# &nbsp; close DECIMAL(18,6),

# &nbsp; volume BIGINT,

# &nbsp; sma\_20 DECIMAL(18,6),

# &nbsp; sma\_50 DECIMAL(18,6),

# &nbsp; daily\_return DECIMAL(18,6),

# &nbsp; created\_at TIMESTAMP DEFAULT CURRENT\_TIMESTAMP,

# &nbsp; CONSTRAINT uniq\_symbol\_date UNIQUE (symbol, trade\_date)

# );

# 

# CREATE INDEX idx\_symbol\_date ON daily\_prices (symbol, trade\_date);

# ```

# 

# ---

# 

# \## ⚙️ Running ETL

# Run the pipeline to extract, transform, and load data into MySQL:

# 

# ```bash

# cd Mid\_FunDS

# python -m src.etl.run\_etl

# ```

# 

# Steps:

# \- `\[EXTRACT]` Load raw CSV file  

# \- `\[TRANSFORM]` Clean data \& compute SMA 20, SMA 50, Daily Return  

# \- `\[LOAD]` Insert into MySQL  

# 

# ---

# 

# \## 📊 Running Dashboards

# 

# \### 1. Streamlit

# ```bash

# streamlit run src/dashboard/dashboard.py

# ```

# Browser: \[http://localhost:8501](http://localhost:8501)

# 

# \### 2. Plotly Dash

# ```bash

# python src/dashboard/app.py

# ```

# Browser: \[http://127.0.0.1:8050](http://127.0.0.1:8050)

# 

# ---

# 

# \## 📈 Features

# \- Interactive stock price charts  

# \- Compare SMA 20 and SMA 50  

# \- Analyze \*\*Daily Return (%)\*\*  

# \- Filter by symbol and time range  

# 

# ---

# 

# \## 📬 Contact

# Email: huyquan1607@gmail.com

# 

# ---

