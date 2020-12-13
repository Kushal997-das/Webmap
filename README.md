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

#### That's how the map look like after executing the code.<br><br>

<a href=https://www.latlong.net/>How to check the latitide and Longitude for any location:</a><br><br>

#### In the above map we are unable to find the exact location right? That's the reason we are using icon for this and also use popup for displaying the location name.<br>

```python3
folium.Marker(location=[46.961580, -102.560670],popup='india',icon=folium.Icon(icon='cloud')).add_to(m)
```

<img align='center' alt='png' width='300px' src="https://github.com/Kushal997-das/Webmap/blob/master/Images/output2.png"/>

#### That's how the map look like after executing the code. <br><br>


### Now we are going to locate three famous places in India using their Latitude and Longitude and put the image over the location.So that we can easily find out where the locations are:
- Ayodhya RamMandir.
- Taj Mahal.
- Ladakh.
<br><br>

```python3
m = folium.Map(tiles='Stamen Toner', zoom_start=4)
ladakh = folium.features.CustomIcon("ladakh.jpg", icon_size=(100,100))
taj_mahhel = folium.features.CustomIcon("taj mahel.jpg", icon_size=(100,100))
rammandir= folium.features.CustomIcon("rammandir.jpg", icon_size=(100, 100))
folium.Marker([40.743720, -73.822030], tooltip="Ladakh", popup='Ladakh,India', icon=ladakh).add_to(m)
folium.Marker([39.760979, -84.192200], tooltip="Taj Mahal", popup='Taj Mahal,India', icon=taj_mahhel).add_to(m)
folium.Marker([54.464180, -110.182259], tooltip="Ayodhya RamMandir", popup='Ayodhya RamMandir,India', icon=rammandir).add_to(m)
```
<br>

<img align='center' alt='png' width='300px' src="https://github.com/Kushal997-das/Webmap/blob/master/Images/outpu3.png"/>
