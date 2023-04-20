import random
import pandas as pd


class Fund:
	""" Class for an equity fund. """
	# Public class variable (equal for all objects)
	owner_name = "Broke Brokers Inc."

	# Constructor - initializes object
	def __init__(self, fund_name, start_cash=100000.0):
		self._name = fund_name
		self._cash = start_cash
		self._portfolio = {}	# Dict of PortfolioEntry-objects with ticker as key


	def portfolio_as_dataframe(self):
		"""Returns the portfolio as a Pandas DataFrame."""
		df_portfolio = pd.DataFrame(columns=["ticker", "company_name", "price_bought", "price_now", "volume"])
		for key, value in self._portfolio.items():
			entry_df = pd.DataFrame(value.to_list(), index=["ticker", "company_name", "price_bought", "price_now", "volume"])
			entry_df_transp = entry_df.transpose()
			df_portfolio = pd.concat([df_portfolio, entry_df_transp], ignore_index=True)
		return df_portfolio


	def buy_stock(self, stock, volume):
		"""Takes a stock object and volume."""
		ticker, c_name, price = stock.to_list()
		# Check if stock is already in portfolio
		if ticker in self._portfolio:
			# If so, add volume only
			self._portfolio[ticker].volume += volume
		else:
			# If not, make a new entry in the portfolio (PortfolioEntry object)
			self._portfolio[ticker] = PortfolioEntry(ticker, c_name, price, price, volume)
		# Update cash holding
		self._cash = self._cash - volume*price


	def update_price(self, ticker, price_new):
		"""Takes a ticker and prices, and updates the price of this stocks in the portfolio."""
		self._portfolio[ticker].price_now = price_new


	def get_value(self, nice=False):
		"""Returns a list with three elements: Cash Value, Assets Value, Total Value."""
		cash_value = self._cash
		assets_value = 0
		for ticker, entry in self._portfolio.items():
			assets_value += entry.price_now*entry.volume
		total_value = cash_value + assets_value
		if nice:
			return f"Cash Value: {cash_value}\nAssets Value: {assets_value}\nTotal Value: {total_value}"
		return [cash_value,assets_value,total_value]


	def get_portfolio(self):
		"""Returns the dict of PortfolioEntry-objects with ticker as key."""
		return self._portfolio




class PortfolioEntry:
	"""Class describing an entry/row in a portfolio."""
	def __init__(self, ticker, company_name, price_bought, price_now, volume):
		"""Takes five arguments: Ticker, Company name, Price (bought), Price (now), Volume."""
		self.ticker = ticker 
		self.company_name = company_name
		self.price_bought = price_bought
		self.price_now = price_now
		self.volume = volume


	def get_price_now(self):
		return self.price_now


	def update_price(self, price_new):
		self.price_now = price_new


	def to_list(self):
		"""Returns a list of the variables in this PortfolioEntry."""
		return [self.ticker,self.company_name,self.price_bought,self.price_now,self.volume]



class Stock:
	"""Class describing stocks."""
	def __init__(self, ticker, company_name, price):
		self._ticker = ticker
		self._company_name = company_name
		self._price = price


	def get_price(self):
		"""Returns the price of the stock."""
		return self._price


	def to_list(self):
		"""Returns all Stock variables as a list."""
		return [self._ticker, self._company_name, self._price]


	def update_price(self):
		"""Creates new stockprice randomly."""
		new_price = self._price*(1+random.uniform(-1,1)*3/100)  # +/- 0-3% change
		self._price = new_price




if __name__ == "__main__":
	print("Executed when invoked directly")
