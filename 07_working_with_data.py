'''
Get 7 days of weather
The Open-Meteo API can give us historical data:

'''

import requests
from datetime import datetime, timedelta

#Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7) #calculates date of week ago

# Formate dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d") 
end_date = today.strftime("%Y-%m-%d")
#strftime() means String Format Time.


# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"


response = requests.get(url)
data = response.json()
print(data)



###  Load into pandas
# Now let’s organize this data:
import pandas as pd

# Extract the daily data
daily_data = data['daily']

#Create a daaframe
df = pd.DataFrame({
    'date':daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})
print(df['date'])
#convert date string to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)


## Visualize the data
#Create a simple line chart:

import matplotlib.pyplot as plt


# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()


## Save to CSV
# Let’s save our data for later use:

import os

# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/paris_weather.csv', index=False)
print("Data saved to data/paris_weather.csv")