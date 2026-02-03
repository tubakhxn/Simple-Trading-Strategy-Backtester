# Trading Strategy Backtester

A Python project to backtest a Simple Moving Average (SMA) crossover strategy on historical stock data.

## Features
- Download historical stock data using Yahoo Finance
- Implement SMA crossover strategy
- Generate buy and sell signals
- Backtest with initial capital
- Calculate total return, win rate, and maximum drawdown
- Plot stock price with buy/sell signals and equity curve

## Strategy Explanation
The SMA crossover strategy uses two moving averages:
- **Short SMA**: Fast-moving average (e.g., 50 days)
- **Long SMA**: Slow-moving average (e.g., 200 days)

**Buy Signal**: When the short SMA crosses above the long SMA.
**Sell Signal**: When the short SMA crosses below the long SMA.

## Backtesting Logic
- Start with an initial capital
- Buy shares when a buy signal is generated
- Sell all shares when a sell signal is generated
- Track equity curve and calculate performance metrics

## How to Run
1. Clone or download this repository
2. Create and activate a Python 3 virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the main script:
   ```bash
   python main.py
   ```

## Example Graphs
- **Price Chart with Buy/Sell Signals**
- **Equity Curve Over Time**

## Author
- tubakhxn

## Forking & Contribution Guide
1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Submit a pull request with a clear description
4. Ensure code is well-documented and tested

---
Happy Backtesting!
