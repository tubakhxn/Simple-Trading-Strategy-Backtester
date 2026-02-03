import matplotlib.pyplot as plt

def plot_signals(data, signals, ticker):
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['Close'], label=f'{ticker} Price', color='blue')
    plt.plot(signals.index, signals['short_sma'], label='Short SMA', color='green')
    plt.plot(signals.index, signals['long_sma'], label='Long SMA', color='red')
    buy_signals = signals[signals['positions'] == 1]
    sell_signals = signals[signals['positions'] == -1]
    plt.scatter(buy_signals.index, buy_signals['price'], marker='^', color='g', label='Buy Signal', s=100)
    plt.scatter(sell_signals.index, sell_signals['price'], marker='v', color='r', label='Sell Signal', s=100)
    plt.title(f'{ticker} Price with SMA Signals')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_equity_curve(results):
    plt.figure(figsize=(14, 5))
    plt.plot(results.index, results['equity'], label='Equity Curve', color='purple')
    plt.title('Equity Curve Over Time')
    plt.xlabel('Date')
    plt.ylabel('Equity ($)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
