import requests
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime, timedelta
#--------------------------------------------------------------
# Fetching data from Open-Meteo API for Paris (latitude: 48.85, longitude: 2.35)
# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Baghdad weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=33.31&longitude=44.36&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

#--------------------------------------------------------------
# Processing the data
# Extract the daily data
daily_data = data['daily']
elevation = data['elevation']
# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime because Json returns dates as strings
df['date'] = pd.to_datetime(df['date'])

print(df)


#-------------------------------------------------------------
# Plotting the data
# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Baghdad Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()

#--------------------------------------------------------------
# Saving the data to a CSV file


# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/Baghdad_weather.csv', index=False)
print("Data saved to data/paris_weather.csv")