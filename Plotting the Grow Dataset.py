import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point

# Read the dataset into a Pandas DataFrame
df = pd.read_csv('C:\Users\kkart\Desktop\ASSIGNMENTS\Python 2 6th\Archive\GrowLocations.csv')  

# Data cleaning: Filtering incorrect latitude and longitude values
# Assuming latitude is in a column named 'Longitude' and longitude in 'Latitude'
df = df[(df['Longitude'] >= 50.681) & (df['Longitude'] <= 57.985) &
        (df['Latitude'] >= -10.592) & (df['Latitude'] <= 1.6848)]

# Converting DataFrame to a GeoDataFrame
geometry = [Point(xy) for xy in zip(df['Latitude'], df['Longitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')

# Load the map 
uk_map = gpd.read_file('C:\Users\kkart\Desktop\ASSIGNMENTS\Python 2 6th\Archive\map7.png')

# Plotting the UK map
fig, ax = plt.subplots(figsize=(10, 10))
uk_map.plot(ax=ax, alpha=0.4, color='grey')

# Plotting the sensor locations on the map
gdf.plot(ax=ax, markersize=10, color='red', marker='o', label='Sensor Locations')

# Set plot title and legend
plt.title('GROW Sensor Locations on UK Map')
plt.legend()

# Show the plot
plt.show()