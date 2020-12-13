Folium
-------
- Folium is a powerful Python library that helps you create several types of Leaflet maps. ... To get an idea, just zoom/click around on the next map to get an impression. 



Pre-requisites:
--------------
    Python
    folium
Installation:
------------



    $ pip install folium

or


    $ conda install -c conda-forge folium

### Importing module:
```python3
import folium
```
### creating a map object:
```python3
m = folium.Map(tiles='Stamen Toner', zoom_start=4)
#different tiles (map styles) can be used, like 'Stamen Toner', 'Stamen Terrain', ...
```
```python3
m = folium.Map(location=[46.961580, -102.560670], tiles='Mapbox Bright', zoom_start=4)
#m = folium.Map(location=[Latitude, Longitude])
```

<img align="Center" alt="GIF"  width="300px" src="https://github.com/Kushal997-das/Webmap/blob/master/Images/output1.png" />

#### That's how the map look like after executing the code.<br>

<a href=https://www.latlong.net/>How to check the latitide and Longitude for any location:</a><br>

#### In the above map we are unable to find the exact location right? That's the reason we are using icon for this and also use popup for displaying the location name.<br>

```python3
folium.Marker(location=[46.961580, -102.560670],popup='india',icon=folium.Icon(icon='cloud')).add_to(m)
```

<img align='center' alt='png' width='300px' src="https://github.com/Kushal997-das/Webmap/blob/master/Images/output2.png"/>

#### That's how the map look like after executing the code. <br>


#create city markers and add them to map object
folium.Marker(location=[26.787964, -82.198555],popup='Ayodhya RamMandir',icon=folium.Icon(icon='cloud')).add_to(m)
folium.Marker(location=[27.175014, -78.042152],popup='Taj Mahal',icon=folium.Icon(color='place')).add_to(m)
folium.Marker(location=[35.447601, -76.274803],popup='Ladakh',icon=folium.Icon(color='red', icon='mandir')).add_to(m)
m

