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
