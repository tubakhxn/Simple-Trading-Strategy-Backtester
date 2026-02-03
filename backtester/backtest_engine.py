import pandas as pd

class BacktestEngine:
    def __init__(self, initial_capital=10000):
        self.initial_capital = initial_capital

    def run_backtest(self, data, signals):
        cash = self.initial_capital
        shares = 0
        equity_curve = []
        trade_marks = []
        close_prices = data['Close'].values
        for i in range(len(data)):
            trade = None
            pos_val = float(signals['positions'].iat[i])
            price = close_prices[i]
            if pos_val == 1.0 and shares == 0:  # Buy only if not already holding
                shares = cash // price
                cash -= shares * price
                trade = 'buy'
            elif pos_val == -1.0 and shares > 0:  # Sell only if holding
                cash += shares * price
                trade = 'sell'
                shares = 0
            equity_value = cash + shares * price
            equity_curve.append(equity_value)
            trade_marks.append(trade)
        # Ensure price is 1D array
        price_1d = data['Close'].values.flatten() if len(data['Close'].values.shape) > 1 else data['Close'].values
        results = pd.DataFrame({
            'equity': equity_curve,
            'price': price_1d,
            'trades': trade_marks
        }, index=data.index)
        return results
