import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import numpy as np

# Historical data from your image (simplified)
dates_historical = [
    datetime(2009, 1, 1),  # Bitcoin was launched, no market price yet
    datetime(2009, 2, 1), datetime(2009, 3, 1), datetime(2009, 4, 1), datetime(2009, 5, 1), datetime(2009, 6, 1),
    datetime(2009, 7, 1), datetime(2009, 8, 1), datetime(2009, 9, 1), datetime(2009, 10, 1), datetime(2009, 11, 1), datetime(2009, 12, 1),
    datetime(2010, 1, 1), datetime(2010, 2, 1), datetime(2010, 3, 1), datetime(2010, 4, 1), datetime(2010, 5, 1), datetime(2010, 6, 1),
    datetime(2010, 7, 1), datetime(2010, 8, 1), datetime(2010, 9, 1), datetime(2010, 10, 1), datetime(2010, 11, 1), datetime(2010, 12, 1),
    datetime(2011, 1, 1), datetime(2011, 2, 1), datetime(2011, 3, 1), datetime(2011, 4, 1), datetime(2011, 5, 1), datetime(2011, 6, 1),
    datetime(2011, 7, 1), datetime(2011, 8, 1), datetime(2011, 9, 1), datetime(2011, 10, 1), datetime(2011, 11, 1), datetime(2011, 12, 1),
    datetime(2012, 1, 1), datetime(2012, 2, 1), datetime(2012, 3, 1), datetime(2012, 4, 1), datetime(2012, 5, 1), datetime(2012, 6, 1),
    datetime(2012, 7, 1), datetime(2012, 8, 1), datetime(2012, 9, 1), datetime(2012, 10, 1), datetime(2012, 11, 1), datetime(2012, 12, 1),
    datetime(2013, 1, 1), datetime(2013, 2, 1), datetime(2013, 3, 1), datetime(2013, 4, 1), datetime(2013, 5, 1), datetime(2013, 6, 1),
    datetime(2013, 7, 1), datetime(2013, 8, 1), datetime(2013, 9, 1), datetime(2013, 10, 1), datetime(2013, 11, 1), datetime(2013, 12, 1),
    datetime(2014, 1, 1), datetime(2014, 2, 1), datetime(2014, 3, 1), datetime(2014, 4, 1), datetime(2014, 5, 1), datetime(2014, 6, 1),
    datetime(2014, 7, 1), datetime(2014, 8, 1), datetime(2014, 9, 1), datetime(2014, 10, 1), datetime(2014, 11, 1), datetime(2014, 12, 1),
    datetime(2015, 1, 1), datetime(2015, 2, 1), datetime(2015, 3, 1), datetime(2015, 4, 1), datetime(2015, 5, 1), datetime(2015, 6, 1),
    datetime(2015, 7, 1), datetime(2015, 8, 1), datetime(2015, 9, 1), datetime(2015, 10, 1), datetime(2015, 11, 1), datetime(2015, 12, 1),
    datetime(2016, 1, 1), datetime(2016, 2, 1), datetime(2016, 3, 1), datetime(2016, 4, 1), datetime(2016, 5, 1), datetime(2016, 6, 1),
    datetime(2016, 7, 1), datetime(2016, 8, 1), datetime(2016, 9, 1), datetime(2016, 10, 1), datetime(2016, 11, 1), datetime(2016, 12, 1),
    datetime(2017, 1, 1), datetime(2017, 2, 1), datetime(2017, 3, 1), datetime(2017, 4, 1), datetime(2017, 5, 1), datetime(2017, 6, 1),
    datetime(2017, 7, 1), datetime(2017, 8, 1), datetime(2017, 9, 1), datetime(2017, 10, 1), datetime(2017, 11, 1), datetime(2017, 12, 1),
    datetime(2018, 1, 1), datetime(2018, 2, 1), datetime(2018, 3, 1), datetime(2018, 4, 1), datetime(2018, 5, 1), datetime(2018, 6, 1),
    datetime(2018, 7, 1), datetime(2018, 8, 1), datetime(2018, 9, 1), datetime(2018, 10, 1), datetime(2018, 11, 1), datetime(2018, 12, 1),
    datetime(2019, 1, 1), datetime(2019, 2, 1), datetime(2019, 3, 1), datetime(2019, 4, 1), datetime(2019, 5, 1), datetime(2019, 6, 1),
    datetime(2019, 7, 1), datetime(2019, 8, 1), datetime(2019, 9, 1), datetime(2019, 10, 1), datetime(2019, 11, 1), datetime(2019, 12, 1),
    datetime(2020, 1, 1), datetime(2020, 2, 1), datetime(2020, 3, 1), datetime(2020, 4, 1), datetime(2020, 5, 1), datetime(2020, 6, 1),
    datetime(2020, 7, 1), datetime(2020, 8, 1), datetime(2020, 9, 1), datetime(2020, 10, 1), datetime(2020, 11, 1), datetime(2020, 12, 1),
    datetime(2021, 1, 1), datetime(2021, 2, 1), datetime(2021, 3, 1), datetime(2021, 4, 1), datetime(2021, 5, 1), datetime(2021, 6, 1),
    datetime(2021, 7, 1), datetime(2021, 8, 1), datetime(2021, 9, 1), datetime(2021, 10, 1), datetime(2021, 11, 1), datetime(2021, 12, 1),
    datetime(2022, 1, 1), datetime(2022, 2, 1), datetime(2022, 3, 1), datetime(2022, 4, 1), datetime(2022, 5, 1), datetime(2022, 6, 1),
    datetime(2022, 7, 1), datetime(2022, 8, 1), datetime(2022, 9, 1), datetime(2022, 10, 1), datetime(2022, 11, 1), datetime(2022, 12, 1),
    datetime(2023, 1, 1), datetime(2023, 2, 1), datetime(2023, 3, 1), datetime(2023, 4, 1), datetime(2023, 5, 1), datetime(2023, 6, 1),
    datetime(2023, 7, 1), datetime(2023, 8, 1), datetime(2023, 9, 1), datetime(2023, 10, 1), datetime(2023, 11, 1), datetime(2023, 12, 1),
    datetime(2024, 1, 1), datetime(2024, 2, 1), datetime(2024, 3, 1), datetime(2024, 4, 1), datetime(2024, 5, 1), datetime(2024, 6, 1),
    datetime(2024, 7, 1), datetime(2024, 8, 1), datetime(2024, 9, 1), datetime(2024, 10, 1), datetime(2024, 11, 1), datetime(2024, 12, 1),
    datetime(2025, 1, 1)
]
prices_historical = [
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
    104809.00  # January 2025
]

# Extrapolate until 2100
last_date = dates_historical[-1]
years_to_extrapolate = 2100 - last_date.year
dates_extrapolated = []
prices_extrapolated = []

current_date = last_date
current_price = prices_historical[-1]

for year in range(last_date.year + 1, 2101):
    for month in range(1, 13):
        # Add a month
        current_date += timedelta(days=30)
        dates_extrapolated.append(current_date)
        
        # Simple exponential growth model with halving effect
        # Here we assume growth rate decreases over time but increases post-halving
        growth_rate = 0.15  # Initial growth rate
        if (year - last_date.year) % 4 == 0 and month == 5:  # Halving event every 4 years around May
            growth_rate *= 1.5  # Increase growth rate post-halving
            
        # Apply growth with diminishing returns
        current_price *= (1 + growth_rate / (1 + (year - last_date.year) / 10))
        prices_extrapolated.append(current_price)

# Combine historical and extrapolated data
dates_full = dates_historical + dates_extrapolated
prices_full = prices_historical + prices_extrapolated

# Bitcoin halving dates
halving_dates = [
    datetime(2012, 11, 28),
    datetime(2016, 7, 9),
    datetime(2020, 5, 11),
    datetime(2024, 4, 19),
    datetime(2028, 5, 1), datetime(2032, 5, 1), datetime(2036, 5, 1), datetime(2040, 5, 1),
    datetime(2044, 5, 1), datetime(2048, 5, 1), datetime(2052, 5, 1), datetime(2056, 5, 1),
    datetime(2060, 5, 1), datetime(2064, 5, 1), datetime(2068, 5, 1), datetime(2072, 5, 1),
    datetime(2076, 5, 1), datetime(2080, 5, 1), datetime(2084, 5, 1), datetime(2088, 5, 1),
    datetime(2092, 5, 1), datetime(2096, 5, 1)
]

# Create the plot
fig, ax = plt.subplots(figsize=(20, 10))

# Plot the price data
ax.plot(dates_full, prices_full, marker='o', linestyle='-', color='blue', label='Bitcoin Price')

# Add vertical lines for halving events
for i, date in enumerate(halving_dates):
    ax.axvline(date, color='red', linestyle='--', alpha=0.5, label=f'Halving {i+1}' if i == 0 else "")

# Set the title and labels
ax.set_title('Bitcoin Price History and Extrapolation with Halving Events', fontsize=16)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Price in USD (Log Scale)', fontsize=12)

# Use log scale for y-axis
ax.set_yscale('log')

# Format x-axis to show years
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_major_locator(mdates.YearLocator(10))  # Show every 10 years for clarity
plt.xticks(rotation=45)

# Add legend
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), loc='upper left')

# Adjust layout
plt.tight_layout()

# Save the figure since we can't show it interactively
plt.savefig('bitcoin_price_history_extrapolated_v1.png', dpi=300, bbox_inches='tight')

# Optionally, try to show if in an interactive environment
try:
    plt.show()
except:
    print("Plot cannot be displayed interactively here. Check the saved image file.")