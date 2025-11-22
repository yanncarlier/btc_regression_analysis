import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd
# Read data from CSV
df = pd.read_csv('bitcoin_monthly_prices.csv', parse_dates=['date'])
dates = df['date'].tolist()
prices = df['price_usd'].tolist()
# Halving dates (historical + next projected)
halving_dates = [
    datetime(2012, 11, 28),
    datetime(2016, 7, 9),
    datetime(2020, 5, 11),
    datetime(2024, 4, 19),
    datetime(2028, 4, 1),    # Projected
]
# Create the plot
fig, ax = plt.subplots(figsize=(15, 10))
# Plot the price data
ax.plot(dates, prices, marker='o', linestyle='-',
        color='blue', label='Bitcoin Price')
# Add vertical lines for halving events
for i, date in enumerate(halving_dates):
    ax.axvline(date, color='red', linestyle='--', alpha=0.7,
               label='Halving' if i == 0 else "")
# Formatting
ax.set_title('Bitcoin Price History with Halving Events', fontsize=16)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Price in USD (Log Scale)', fontsize=12)
ax.set_yscale('log')
# X-axis: show every year
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_major_locator(mdates.YearLocator())
plt.xticks(rotation=45)
# Legend (deduplicated)
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), loc='upper left')
plt.tight_layout()
plt.savefig('bitcoin_price_history_v1.png', dpi=300, bbox_inches='tight')
# plt.show()   # <-- Delete this line (or comment it)
print("Plot saved as bitcoin_price_history_v1.png")
