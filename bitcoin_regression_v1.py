import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# Historical Bitcoin price data
data = {
    'Date': pd.date_range(start='2013-01-01', end='2025-11-01', freq='MS'),
    'Price': [
        0.00,  # 2009 no price
        0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,  # 2009 Feb-Dec
        0.00, 0.00, 0.00, 0.00, 0.00, 0.00,  # 2010 Jan-Jun
        0.05, 0.06, 0.05, 0.08, 0.39, 0.25,  # 2010
        0.29, 0.75, 0.70, 0.79, 7, 17, 13, 8, 6, 3, 2.80, 3,  # 2011
        5.27, 4.92, 4.74, 4.89, 5.20, 5.77, 6.63, 10.28, 11.43, 11.03, 10.73, 13.30,  # 2012
        13.45, 21.47, 48.87, 127.86, 117.33, 105.51, 80.89, 95.89, 124.33, 184.39, 386.12, 737.16,  # 2013
        819.11, 591.07, 629.59, 461.02, 459.58, 638.41, 641.83, 492.45, 454.81, 352.63, 385.54, 327.54,  # 2014
        259.40, 232.90, 267.67, 233.71, 237.97, 248.95, 287.76, 236.48, 230.46, 267.96, 329.37, 434.55,  # 2015
        432.26, 387.35, 412.92, 442.74, 449.79, 564.93, 650.60, 570.92, 602.88, 627.87, 709.23, 756.96,  # 2016
        886.75, 1021.19, 1247.60, 1148.89, 1747.11, 2479.66, 2530.20, 4067.48, 4179.56, 5834.43, 7498.03, 13809.29,  # 2017
        11376.86, 9343.31, 8359.84, 7891.87, 8031.20, 6795.58, 7374.52, 6344.98, 6561.80, 6513.05, 4209.53, 3826.46,  # 2018
        3663.66, 3517.34, 3916.89, 5194.60, 7279.17, 10849.57, 10161.53, 9973.10, 9677.82, 8115.06, 8737.24, 7194.44,  # 2019
        8515.30, 9548.51, 6450.22, 7862.80, 9353.87, 9107.25, 9376.66, 11596.90, 10726.83, 12166.11, 16901.37, 23359.91,  # 2020
        34200.00, 48513.70, 55667.05, 56295.52, 47396.53, 36608.04, 33443.50, 46619.29, 45154.65, 57405.00, 58354.00, 47776.00,  # 2021
        43056.50, 39283.48, 42277.50, 41047.00, 30375.98, 20614.50, 21377.50, 22209.00, 19480.00, 19532.00, 17119.00, 16520.00,  # 2022
        22766.00, 23136.00, 28436.00, 29312.00, 27971.00, 30182.00, 29070.00, 25958.00, 27200.00, 34446.00, 36768.00, 42224.00,  # 2023
        43000.00, 51000.00, 73608.00, 68000.00, 65000.00, 60000.00, 55000.00, 62000.00, 68000.00, 75000.00, 98117.69, 103679.00,  # 2024
        104809.00, 84373.01, 82548.91, 94207.31, 104638.09, 107135.33, 115758.20, 108236.71, 114056.08, 109556.16, 85090.69  # 2025
    ]
}
# Convert data to DataFrame
df = pd.DataFrame(data)
# Convert Date to numerical format (e.g., days since the first data point)
df['NumericDate'] = (df['Date'] - df['Date'].min()).dt.days
# Fit linear regression model
X = df[['NumericDate']]
y = df['Price']
reg = LinearRegression().fit(X, y)
# Predict Bitcoin price for 2030
future_date = (pd.to_datetime('2030-01-01') - df['Date'].min()).days
predicted_price = reg.predict([[future_date]])
# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(df['Date'], df['Price'], color='blue', label='Historical Prices')
plt.plot(df['Date'], reg.predict(X), color='red',
         linewidth=2, label='Linear Regression')
plt.title('Bitcoin Price Prediction for 2030')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.axvline(x=pd.to_datetime('2030-01-01'), color='green',
            linestyle='--', label='Prediction for 2030')
plt.legend()
plt.grid(True)
plt.show()
print("Predicted Bitcoin price for 2030:", predicted_price[0])
