import pytest

class Stock():
    def __init__(self):
        self.prices = []

    def buy_and_sell_stock_once(self):
        max_profit = 0
        for buying in range(len(self.prices)-1):
            for selling in range(buying+1, len(self.prices)):
                profit = self.prices[selling] - self.prices[buying]
                if profit > max_profit and profit > 0:
                    max_profit = profit 
        
        return max_profit

class TestStock():
    def test_sell_buy(self):
        stock = Stock()

        stock.prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

        assert 30 == stock.buy_and_sell_stock_once()


