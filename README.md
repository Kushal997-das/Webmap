# Searching
```python3
#importing modle
import folium

#create map object
#different tiles (map styles) can be used, like 'Stamen Toner', 'Stamen Terrain', ...
m = folium.Map(location=[46.961580, -102.560670],tiles='Stamen Toner', zoom_start=4)
#create city markers and add them to map object
folium.Marker(location=[26.787964, -82.198555],popup='Ayodhya RamMandir',icon=folium.Icon(icon='cloud')).add_to(m)
folium.Marker(location=[27.175014, -78.042152],popup='Taj Mahal',icon=folium.Icon(color='place')).add_to(m)
folium.Marker(location=[35.447601, -76.274803],popup='Ladakh',icon=folium.Icon(color='red', icon='mandir')).add_to(m)
m
```
