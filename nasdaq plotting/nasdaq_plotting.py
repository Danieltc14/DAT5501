
import pandas as pd
import plotly.express as px

# Load Tesla historical data from CSV
df = pd.read_csv('HistoricalData_1763980159179.csv')

# Clean the dataset
# Convert Date to datetime and sort ascending
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Clean Close/Last column: strip '$' and convert to float
df['Close'] = df['Close/Last'].apply(lambda x: float(x.replace('$', '').strip()))

# Calculate daily percentage change
df['Pct_Change'] = df['Close'].pct_change() * 100

# Compute standard deviation of daily percentage changes
std_dev = df['Pct_Change'].std()
print(f"Standard Deviation of Tesla Daily % Changes: {std_dev:.2f}%")

# Plot Closing Price vs Date
fig_price = px.line(df, x='Date', y='Close',
                    title='Tesla Closing Price (Last 1 Year)',
                    labels={'Date': 'Date', 'Close': 'Closing Price ($)'})
fig_price.show()

# Plot Daily Percentage Change vs Date
fig_pct = px.line(df, x='Date', y='Pct_Change',
                  title='Tesla Daily Percentage Change',
                  labels={'Date': 'Date', 'Pct_Change': 'Daily % Change'})
fig_pct.show()

# Export cleaned dataset with percentage change column
df.to_csv('tesla_cleaned.csv', index=False)
