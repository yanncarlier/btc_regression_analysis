import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import numpy as np
from bisect import bisect_left

# Function to find the index of the closest date in date_list to target_date
def find_closest_date(date_list, target_date):
    pos = bisect_left(date_list, target_date)
    if pos == 0:
        return 0
    if pos == len(date_list):
        return len(date_list) - 1
    before = date_list[pos - 1]
    after = date_list[pos]
    return pos if (after - target_date) < (target_date - before) else pos - 1

# Function to extrapolate Bitcoin prices considering halving cycles
def extrapolate_bitcoin_price(dates_historical, prices_historical, end_year=2100):
    last_date = dates_historical[-1]
    last_price = prices_historical[-1]

    # Bitcoin halving dates (historical and projected)
    halving_dates = [
        datetime(2012, 11, 28), datetime(2016, 7, 9), datetime(2020, 5, 11), datetime(2024, 4, 19),
        datetime(2028, 5, 1), datetime(2032, 5, 1), datetime(2036, 5, 1), datetime(2040, 5, 1),
        datetime(2044, 5, 1), datetime(2048, 5, 1), datetime(2052, 5, 1), datetime(2056, 5, 1),
        datetime(2060, 5, 1), datetime(2064, 5, 1), datetime(2068, 5, 1), datetime(2072, 5, 1),
        datetime(2076, 5, 1), datetime(2080, 5, 1), datetime(2084, 5, 1), datetime(2088, 5, 1),
        datetime(2092, 5, 1), datetime(2096, 5, 1)
    ]
    while halving_dates[-1].year < end_year:
        halving_dates.append(halving_dates[-1] + timedelta(days=4 * 365))

    # Find historical halving indices and calculate cycle CAGRs
    halving_indices = [find_closest_date(dates_historical, date) for date in halving_dates if date <= last_date]
    cycle_cagrs = []
    for i in range(len(halving_indices) - 1):
        start_price = prices_historical[halving_indices[i]]
        end_price = prices_historical[halving_indices[i + 1]]
        years_between = (dates_historical[halving_indices[i + 1]] - dates_historical[halving_indices[i]]).days / 365.25
        if years_between > 0 and start_price > 0 and end_price > 0:
            cagr = (end_price / start_price) ** (1 / years_between) - 1
            cycle_cagrs.append(cagr)
    
    # Use average CAGR if available, otherwise default to 20%
    avg_cagr = np.mean(cycle_cagrs) if cycle_cagrs else 0.20

    # Extrapolation setup
    dates_extrapolated = []
    prices_extrapolated = []
    current_date = last_date
    current_price = last_price

    while current_date.year < end_year:
        current_date += timedelta(days=30)
        dates_extrapolated.append(current_date)

        # Determine position within the current halving cycle
        cycle_index = bisect_left(halving_dates, current_date) - 1
        if cycle_index < 0:
            cycle_index = 0
        cycle_start = halving_dates[cycle_index]
        cycle_end = halving_dates[min(cycle_index + 1, len(halving_dates) - 1)]
        days_into_cycle = (current_date - cycle_start).days
        cycle_length_days = (cycle_end - cycle_start).days
        cycle_progress = days_into_cycle / cycle_length_days if cycle_length_days > 0 else 0

        # Model cycle phases: simplified as pre-halving growth, post-halving peak, and stabilization
        monthly_growth = avg_cagr / 12  # Base monthly growth from annual CAGR
        if cycle_progress < 0.25:  # First year: moderate growth
            monthly_growth *= 0.8
        elif cycle_progress < 0.5:  # Second year (pre-halving): stronger growth
            monthly_growth *= 1.5
        elif cycle_progress < 0.75:  # Third year (post-halving): peak growth
            monthly_growth *= 2.0
        else:  # Fourth year: stabilization
            monthly_growth *= 0.5

        # Dampen growth over time (reduce by 1% per year after 2025)
        years_from_start = (current_date.year - 2025)
        dampening_factor = max(0.1, 1 - 0.01 * years_from_start)  # Minimum 10% of original growth
        monthly_growth *= dampening_factor

        # Update price with growth and slight volatility
        current_price *= (1 + monthly_growth) * (1 + np.random.normal(0, 0.02))  # 2% volatility
        prices_extrapolated.append(max(current_price, 0))  # Prevent negative prices

    return dates_historical + dates_extrapolated, prices_historical + prices_extrapolated, halving_dates

# Generate historical dates from January 2009 to January 2025
def generate_monthly_dates(start_year, start_month, end_year, end_month):
    dates = []
    current_date = datetime(start_year, start_month, 1)
    end_date = datetime(end_year, end_month, 1)
    while current_date <= end_date:
        dates.append(current_date)
        # Move to the next month
        if current_date.month == 12:
            current_date = datetime(current_date.year + 1, 1, 1)
        else:
            current_date = datetime(current_date.year, current_date.month + 1, 1)
    return dates

# Historical dates from January 2009 to January 2025
dates_historical = generate_monthly_dates(2009, 1, 2025, 1)

# Historical prices (example data; replace with actual prices if available)
# For now, using placeholder prices (all 0.00 except last one for demonstration)
prices_historical = [0.00] * (len(dates_historical) - 1) + [104809.00]

# Extrapolate and get full dates, prices, and halving dates
dates_full, prices_full, halving_dates = extrapolate_bitcoin_price(dates_historical, prices_historical)

# Plotting
fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(dates_full, prices_full, marker='o', linestyle='-', color='blue', label='Bitcoin Price')
for i, date in enumerate(halving_dates):
    ax.axvline(date, color='red', linestyle='--', alpha=0.5, label=f'Halving {i+1}' if i == 0 else "")
ax.set_title('Bitcoin Price History and Extrapolation with Halving Events', fontsize=16)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Price in USD (Log Scale)', fontsize=12)
ax.set_yscale('log')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_major_locator(mdates.YearLocator(10))
plt.xticks(rotation=45)
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), loc='upper left')
plt.tight_layout()
plt.savefig('Bitcoin_price_forecast.png', dpi=300, bbox_inches='tight')
try:
    plt.show()
except:
    print("Plot saved as 'Bitcoin_price_forecast.png'.")