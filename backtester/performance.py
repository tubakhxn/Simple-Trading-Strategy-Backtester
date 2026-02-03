import numpy as np

class PerformanceMetrics:
    def calculate(self, results):
        equity = results['equity']
        total_return = ((equity.iloc[-1] - equity.iloc[0]) / equity.iloc[0]) * 100
        trades = results['trades'].dropna()
        buy_prices = results[results['trades'] == 'buy']['price']
        sell_prices = results[results['trades'] == 'sell']['price']
        wins = (sell_prices.values > buy_prices.values).sum()
        win_rate = (wins / len(buy_prices)) * 100 if len(buy_prices) > 0 else 0
        roll_max = equity.cummax()
        drawdown = (equity - roll_max) / roll_max
        max_drawdown = drawdown.min() * 100
        return {
            'total_return': total_return,
            'win_rate': win_rate,
            'max_drawdown': abs(max_drawdown)
        }
