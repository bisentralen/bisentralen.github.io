import pandas as pd
import matplotlib.pyplot as plt
import equityfundlib as ef


def load_stocks(stocks_file):
	"""Takes a csv file as input, and returns a dict of stock objects."""
	df = pd.read_csv(stocks_file)	# A Pandas DataFrame
	stocks = {}						# An empty dictionary
	for index, row in df.iterrows():
		# Loop over DataFrame, make a Stock object for each line, and save it in a dict
		stocks[row['ticker']] = ef.Stock(row['ticker'], row['company_name'], row['price'])
	return stocks 	# Returning a dict of stocks with ticker as key and Stock object as value


# update stock prices
def update_stock_prices():
	# Update stock objects
	for ticker in stocks:
		stocks[ticker].update_price()
	# Update prices in portfolio
	for ticker in my_fund.get_portfolio():
		my_fund.update_price(ticker, stocks[ticker].get_price())


# Make a dictionary with stock objects with, by calling function load_stocks
stocks = load_stocks("https://bisentralen.github.io/files/data_stocks.csv")
#stocks = load_stocks("https://tinyurl.com/bistocks")

# Make a fund
my_fund = ef.Fund("More is More")

# Buy stocks
my_fund.buy_stock(stocks['bbb'], 500)
my_fund.buy_stock(stocks['nid'], 1000)
my_fund.buy_stock(stocks['nys'], 2500)

# Print fund data
print(my_fund)
print(my_fund.portfolio_as_dataframe())
print("---------------------------------------------------------------------")


update_stock_prices()

# Print fund data
print(my_fund)
print(my_fund.portfolio_as_dataframe())
print("---------------------------------------------------------------------")

# Buy more
my_fund.buy_stock(stocks['nid'], 500)
my_fund.buy_stock(stocks['alu'], 400)

update_stock_prices()

# Print fund data
print(my_fund)
print(my_fund.portfolio_as_dataframe())
print("---------------------------------------------------------------------")


# Sell stocks
my_fund.sell_stock(stocks['bbb'])
my_fund.sell_stock(stocks['nys'], 2000)


# Print fund data
print(my_fund)
print(my_fund.portfolio_as_dataframe())
print("---------------------------------------------------------------------")







#####################################################
# Plot a time series of the total value of the fund

# Store the portfolio in a variable, for easier reading
portfolio = my_fund.get_portfolio()

# Make a list of ascending integers to represent time
x2 = [i for i in range(0,800)]

# Make an empty list to store fund values for each point in time
y_value = []

# For each time, store the value and update prices
for time in x2:
	y_value.append(my_fund.get_value()[2])
	update_stock_prices()

# Make a moving average for value
ma = []
ma_length = 50
# Fill the first ma_length list elements with empty value that is not plotted
for i in range(ma_length-1): 
	ma.append(float("nan"))
# Calculate moving average for each y_value, and put it in the ma list
for i in range(ma_length-1, len(y_value)):
	ma.append(sum(y_value[(i-(ma_length-1)):(i+1)])/ma_length)



# Make the value plot
plt.plot(x2, y_value, label="Total Value")
# Make the moving average plot
plt.plot(x2, ma, label="MA"+str(ma_length)) 
# Descriptive elements
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Fund Value Time Series")
plt.legend()  # Identifies each line in the plot
# Show the plot
plt.show()



