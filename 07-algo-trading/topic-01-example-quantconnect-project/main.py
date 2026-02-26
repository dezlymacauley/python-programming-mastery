# region imports
from AlgorithmImports import *
# endregion

class AdaptableRedOrangeHorse(QCAlgorithm):

    def initialize(self):

        # NOTE: Dezly's Note
        # This is the start date of the backtest

        # Set Start Date
        self.set_start_date(2021, 1, 1)

        # Set cash
        self.set_cash(100000)

        # Add AAPL
        self.AAPL_symbol = self.add_equity("AAPL", Resolution.DAILY).symbol

        # Past data store
        self.past_data = []

    def on_data(self, data: Slice):

        # Store
        self.past_data.append(self.securities[self.AAPL_symbol].close - self.securities[self.AAPL_symbol].open)

        # If not invested
        if self.portfolio[self.AAPL_symbol].invested == False:
            
            # If stored 2 and above
            if len(self.past_data) > 2:

                # If 3 red bars

                # NOTE: Dezly's Note:
                # Trading bot checks the past 3 daily candle sticks of the stock
                # and checks if they are red candles

                if (
                    
                    self.past_data[-3] < 0 and

                    self.past_data[-2] < 0 and

                    self.past_data[-1] < 0

                    ):

                    # NOTE:  Dezly's Note:
                    # If the all the candles are red,
                    # then the trading bot will buy the stock with all of the cash that
                    # it has available.

                    # Quantity
                    quantity = int(self.portfolio.cash / self.securities[self.AAPL_symbol].close)

                    # Buy
                    self.market_order(symbol = self.AAPL_symbol, quantity = quantity)
      
        # NOTE: Dezly's Note
        # If the trading bot is invested in this stock already,
        # then it will not buy again.
        # -----------------------------------------------------------------
        # It will instead run its exit logic which is a `10% take profit`.
        # -----------------------------------------------------------------
        # This means that if the price of the stock is `10%` more than the
        # price that I bought it for, then sell the stock. 
        # ----------------------------------------------------------------
        # This logic will continue to repeat from the `start date` of this
        # back test until today's date.

        # Else
        else:

            # If 10% and above average price
            if self.securities[self.AAPL_symbol].close > self.portfolio[self.AAPL_symbol].average_price * 1.1:
                
                # Sell
                self.market_order(symbol = self.AAPL_symbol, quantity = -self.portfolio[self.AAPL_symbol].quantity)
