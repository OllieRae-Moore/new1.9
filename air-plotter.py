'''
You have been provided with ‘leeds-central-air-quality.csv’ which is a file containing air quality data for Leeds from the last few years. There are 4 values – particulate matter (25), particulate matter (10), Ozone and Nitrous Oxide which are all different measures of air quality – which are recorded against the date.
Load this file into a suitable data structure.

From this data, create a line plot of the average of the 4 data points against the date.

For example, for the row:
07/09/2024,68,20,25,5

You would plot a point at (68+20+25+5)/4 = 29.5

The X-axis should be the date, the Y-axis should be the average pollution.
'''
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("leeds-centre-air-quality.csv")
data["date"] = pd.to_datetime(data['date'])
data['average'] = data[[' pm25',' pm10',' o3',' no2']].mean(axis=1)
plt.figure(figsize=(12,6)) #had to stretch x axis since labels overlapped and its easier to read
plt.plot(data["date"], data['average'])
plt.xlabel("Date")
plt.ylabel("average pollution")
plt.title("Oliver Rae-Moore")
plt.show()
