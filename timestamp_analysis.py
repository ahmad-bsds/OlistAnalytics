import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

# Load the data
PATH_TO_DATA = './Data/2'
orders = pd.read_csv(f'{PATH_TO_DATA}/olist_orders_dataset.csv')

# Convert order_purchase_timestamp to datetime
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])

# Extract date/time features
orders['year'] = orders['order_purchase_timestamp'].dt.year
orders['month'] = orders['order_purchase_timestamp'].dt.month
orders['day'] = orders['order_purchase_timestamp'].dt.day
orders['hour'] = orders['order_purchase_timestamp'].dt.hour
orders['day_of_week'] = orders['order_purchase_timestamp'].dt.dayofweek  # Monday=0, Sunday=6
orders['day_name'] = orders['order_purchase_timestamp'].dt.day_name()
orders['week_of_year'] = orders['order_purchase_timestamp'].dt.isocalendar().week
orders['quarter'] = orders['order_purchase_timestamp'].dt.quarter

# Set up the plotting style
plt.style.use('seaborn-v0_8')
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('Olist Purchase Timestamp Analysis', fontsize=16)

# 1. Hourly Purchase Distribution
hourly_purchases = orders['hour'].value_counts().sort_index()
axes[0, 0].bar(hourly_purchases.index, hourly_purchases.values, color='skyblue')
axes[0, 0].set_title('Purchases by Hour of Day')
axes[0, 0].set_xlabel('Hour of Day')
axes[0, 0].set_ylabel('Number of Purchases')
axes[0, 0].set_xticks(range(0, 24, 2))

# 2. Daily Purchase Distribution
daily_purchases = orders['day_of_week'].value_counts().sort_index()
day_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
axes[0, 1].bar(range(7), daily_purchases.values, color='lightgreen')
axes[0, 1].set_title('Purchases by Day of Week')
axes[0, 1].set_xlabel('Day of Week')
axes[0, 1].set_ylabel('Number of Purchases')
axes[0, 1].set_xticks(range(7))
axes[0, 1].set_xticklabels(day_labels, rotation=45)

# 3. Monthly Purchase Distribution
monthly_purchases = orders['month'].value_counts().sort_index()
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
axes[0, 2].bar(monthly_purchases.index, monthly_purchases.values, color='salmon')
axes[0, 2].set_title('Purchases by Month')
axes[0, 2].set_xlabel('Month')
axes[0, 2].set_ylabel('Number of Purchases')
axes[0, 2].set_xticks(range(1, 13))
axes[0, 2].set_xticklabels(month_labels)

# 4. Yearly Purchase Distribution
yearly_purchases = orders['year'].value_counts().sort_index()
axes[1, 0].bar(yearly_purchases.index.astype(str), yearly_purchases.values, color='gold')
axes[1, 0].set_title('Purchases by Year')
axes[1, 0].set_xlabel('Year')
axes[1, 0].set_ylabel('Number of Purchases')

# 5. Quarterly Purchase Distribution
quarterly_purchases = orders['quarter'].value_counts().sort_index()
axes[1, 1].pie(quarterly_purchases.values, labels=['Q1', 'Q2', 'Q3', 'Q4'], autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
axes[1, 1].set_title('Purchases by Quarter')

# 6. Heatmap of Hour vs Day of Week
pivot_table = orders.groupby(['day_of_week', 'hour']).size().unstack(fill_value=0)
sns.heatmap(pivot_table, ax=axes[1, 2], cmap="YlGnBu")
axes[1, 2].set_title('Purchase Intensity (Hour vs Day of Week)')
axes[1, 2].set_xlabel('Hour of Day')
axes[1, 2].set_ylabel('Day of Week')
axes[1, 2].set_yticks(range(7))
axes[1, 2].set_yticklabels(day_labels)

plt.tight_layout()
plt.show()

# Additional analysis: Peak and non-peak periods
print("=== TIMESTAMP ANALYSIS SUMMARY ===")
print(f"Data range: {orders['order_purchase_timestamp'].min()} to {orders['order_purchase_timestamp'].max()}")

# Peak hours (top 5)
print("\nTop 5 peak hours:")
peak_hours = hourly_purchases.nlargest(5)
for hour, count in peak_hours.items():
    print(f"  {hour}:00 - {count:,} purchases")

# Least busy hours (bottom 5)
print("\n5 least busy hours:")
quiet_hours = hourly_purchases.nsmallest(5)
for hour, count in quiet_hours.items():
    print(f"  {hour}:00 - {count:,} purchases")

# Peak days
print("\nPeak days of week:")
peak_days = daily_purchases.nlargest(3)
for i, (day_idx, count) in enumerate(peak_days.items()):
    print(f"  {i+1}. {day_labels[day_idx]} - {count:,} purchases")

# Peak months
print("\nPeak months:")
peak_months = monthly_purchases.nlargest(3)
for i, (month, count) in enumerate(peak_months.items()):
    print(f"  {i+1}. {month_labels[month-1]} - {count:,} purchases")

# Seasonal analysis
print("\n=== SEASONAL ANALYSIS ===")
# Group by season (Northern Hemisphere seasons)
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

orders['season'] = orders['month'].apply(get_season)
seasonal_purchases = orders['season'].value_counts()
print("Purchases by season:")
for season, count in seasonal_purchases.items():
    print(f"  {season}: {count:,} purchases ({count/len(orders)*100:.1f}%)")

# Weekend vs Weekday analysis
orders['is_weekend'] = orders['day_of_week'].isin([5, 6])  # Saturday=5, Sunday=6
weekend_purchases = orders[orders['is_weekend']]['order_id'].count()
weekday_purchases = orders[~orders['is_weekend']]['order_id'].count()

print(f"\nWeekend purchases: {weekend_purchases:,} ({weekend_purchases/len(orders)*100:.1f}%)")
print(f"Weekday purchases: {weekday_purchases:,} ({weekday_purchases/len(orders)*100:.1f}%)")