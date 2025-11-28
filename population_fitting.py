
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("children-born-per-woman.csv")
data = df[df['Entity'] == 'Afghanistan'][['Year', 'Fertility rate (period), historical']]

years = data['Year'].values
rates = data['Fertility rate (period), historical'].values

# Sub-sample (exclude last 10 years)
sub_years = years[:-10]
sub_rates = rates[:-10]

# Forecast years and actual values
forecast_years = years[-10:]
actual = rates[-10:]

# Fit and forecast polynomials
plt.figure(figsize=(10, 6))
plt.plot(years, rates, 'o-', label='Actual')

for deg in range(1, 10):
    coeffs = np.polyfit(sub_years, sub_rates, deg)
    poly = np.poly1d(coeffs)
    forecast = poly(forecast_years)
    plt.plot(forecast_years, forecast, label=f'Degree {deg}')

plt.title('Polynomial Forecasting (Afghanistan)')
plt.xlabel('Year')
plt.ylabel('Fertility Rate')
plt.legend()
plt.show()
