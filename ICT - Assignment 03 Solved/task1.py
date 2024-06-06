import pandas as pd
import matplotlib.pyplot as plt


def plot_stock_prices(file_path):
    data = pd.read_csv(file_path)

    data['Date'] = pd.to_datetime(data['Date'])

    data = data.sort_values('Date')

    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Close'], label='Closing Price')

    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Stock Closing Prices Over Time')
    plt.legend()

    plt.show()

plot_stock_prices('../Asst-3 data.csv')