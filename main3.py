import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Historical Bitcoin price data
data = {
    'Date': pd.date_range(start='2013-01-01', end='2024-12-01', freq='MS'),
    'Price': [
        13.42, 16.73, 32.00, 230.05, 131.00, 106.00, 67.00, 94.00, 103.00, 127.00, 198.00, 1042.03,
        778.00, 821.00, 604.00, 454.00, 440.00, 581.00, 628.00, 590.00, 515.00, 383.00, 420.00, 375.00,
        313.00, 231.00, 267.00, 223.00, 234.00, 237.00, 262.00, 277.00, 236.00, 239.00, 306.00, 428.00,
        433.00, 368.00, 422.00, 454.00, 445.00, 576.00, 650.00, 603.00, 607.00, 600.00, 713.00, 780.00,
        963.00, 1013.00, 1009.00, 1014.00, 1435.00, 2317.00, 2532.00, 2700.00, 4339.00, 3857.00, 7261.00, 11601.00,
        11601.00, 9640.00, 8973.00, 6714.00, 9341.00, 7556.00, 6655.00, 7324.00, 7142.00, 6321.00, 6380.00, 4299.00,
        3747.00, 3492.00, 3821.00, 4037.00, 5412.00, 7384.00, 11859.00, 10230.00, 9427.00, 8342.00, 9107.00, 7368.00,
        3868.00, 9541.00, 8597.00, 6614.00, 8987.00, 9469.00, 9106.00, 11389.00, 10324.00, 11013.00, 13797.00, 19205.00,
        29331.00, 33498.00, 48238.00, 57774.00, 57286.00, 37639.00, 34947.00, 42505.00, 47529.00, 47973.00, 64025.00, 57778.00,
        47913.00, 36612.00, 38997.00, 45947.00, 58240.00, 34543.00, 31977.00, 43938.00, 46055.00, 57478.00, 64397.00, 48073.00,
        16474.00, 21350.00, 24275.00, 24415.00, 24542.00, 24631.00, 24725.00, 24812.00, 24896.00, 24964.00, 25015.00, 25075.00,
        25136.00, 25155.00, 25171.00, 25188.00, 25202.00, 25215.00, 25227.00, 25239.00, 25251.00, 25261.00, 25273.00, 25284.00
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
plt.plot(df['Date'], reg.predict(X), color='red', linewidth=2, label='Linear Regression')
plt.title('Bitcoin Price Prediction for 2030')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.axvline(x=pd.to_datetime('2030-01-01'), color='green', linestyle='--', label='Prediction for 2030')
plt.legend()
plt.grid(True)
plt.show()

print("Predicted Bitcoin price for 2030:", predicted_price[0])
