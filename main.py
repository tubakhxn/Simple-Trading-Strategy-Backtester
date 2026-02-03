from backtester.strategy import SMACrossoverStrategy
from backtester.backtest_engine import BacktestEngine
from backtester.performance import PerformanceMetrics
from backtester.visualization import plot_signals, plot_equity_curve
import yfinance as yf

# User parameters
TICKER = 'AAPL'
START_DATE = '2020-01-01'
END_DATE = '2023-01-01'
SHORT_WINDOW = 50
LONG_WINDOW = 200
INITIAL_CAPITAL = 10000

# Download historical data
data = yf.download(TICKER, start=START_DATE, end=END_DATE)

# Strategy
strategy = SMACrossoverStrategy(short_window=SHORT_WINDOW, long_window=LONG_WINDOW)
signals = strategy.generate_signals(data)

# Backtest
engine = BacktestEngine(initial_capital=INITIAL_CAPITAL)
results = engine.run_backtest(data, signals)

# Performance
metrics = PerformanceMetrics()
performance = metrics.calculate(results)

# Visualization
plot_signals(data, signals, TICKER)
plot_equity_curve(results)

# Print results
print(f"Total Return: {performance['total_return']:.2f}%")
print(f"Win Rate: {performance['win_rate']:.2f}%")
print(f"Max Drawdown: {performance['max_drawdown']:.2f}%")
