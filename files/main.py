import pandas as pd
import matplotlib.pyplot as plt
import equityfundlib as ef


# update stock prices
def update_stock_prices():
	# Update stock objects
	for ticker in stocks:
		stocks[ticker].update_price()
	# Update prices in portfolio
	for ticker in my_fund.get_portfolio():
		my_fund.update_price(ticker, stocks[ticker].get_price())



# Read CSV file into a Pandas DataFrame
df = pd.read_csv("https://bisentralen.github.io/files/data_stocks.csv")	# A Pandas DataFrame
stocks = {}		# An empty dictionary
for index, row in df.iterrows():
	# Loop over DataFrame, make a Stock object for each line, and save it in a dict
	stocks[row['ticker']] = ef.Stock(row['ticker'], row['company_name'], row['price'])



# Make a fund
my_fund = ef.Fund("More is More")

# Buy stocks
my_fund.buy_stock(stocks['bbb'], 150)
my_fund.buy_stock(stocks['nid'], 1000)
my_fund.buy_stock(stocks['nys'], 1500)

# Print fund data
print(my_fund.get_value("nice"))
print(my_fund.portfolio_as_dataframe())
print("---------------------------------------------------------------------")


update_stock_prices()

# Print fund data
print(my_fund.get_value("nice"))
print(my_fund.portfolio_as_dataframe())
print("---------------------------------------------------------------------")

# Buy more
my_fund.buy_stock(stocks['nid'], 300)
my_fund.buy_stock(stocks['alu'], 400)

update_stock_prices()

# Print fund data
print(my_fund.get_value("nice"))
print(my_fund.portfolio_as_dataframe())
print("---------------------------------------------------------------------")





#####################################################
# Plot a time series of the total value of the fund

# Make a list of ascending integers to represent time
x = [i for i in range(0,1000)]

# Make an empty list to store fund values for each point in time
y = []

# For each time, store the value and update prices
for time in x:
	y.append(my_fund.get_value()[2])
	update_stock_prices()

# Make a moving average for value
ma = []
ma_length = 50
# Fill the first ma_length list elements with empty value that is not plotted
for i in range(ma_length-1): 
	ma.append(float("nan"))
# Calculate moving average for each y, and put it in the ma list
for i in range(ma_length-1, len(y)):
	ma.append(sum(y[(i-(ma_length-1)):(i+1)])/ma_length)



# Make the value plot
plt.plot(x, y, label="Total Value")
# Make the moving average plot
plt.plot(x, ma, label="MA"+str(ma_length)) 
# Descriptive elements
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Fund Value Time Series")
plt.legend()  # Identifies each line in the plot
# Show the plot
plt.show()



