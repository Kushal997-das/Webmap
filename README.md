[![Hello programmer Welcome to this repo](https://img.shields.io/badge/Hello!-Welcometothisrepo-brightgreen.svg?style=flat&logo=github)](https://github.com/kushal997-das)
[![](https://img.shields.io/badge/Author-KushalDas-green.svg)](https://github.com/Kushal997-das)
![](https://img.shields.io/badge/Programming_Language-Python-blue.svg)
![](https://img.shields.io/badge/Status-Complete-green.svg)
[![](https://img.shields.io/github/license/kushal997-das/Webmap.svg?style=plastic)](https://github.com/kushal997-das/Webmap)
[![](https://img.shields.io/github/languages/code-size/kushal997-das/Webmap.svg?style=plastic)](https://github.com/kushal997-das/Webmap)
[![](https://img.shields.io/github/languages/top/kushal997-das/Webmap.svg?style=plastic)](https://github.com/kushal997-das/Webmap)
[![GitHub issues](https://img.shields.io/github/issues/kushal997-das/Webmap.svg)](https://github.com/kushal997-das/Webmap/issues) [![GitHub forks](https://img.shields.io/github/forks/kushal997-das/Webmap.svg)](https://github.com/kushal997-das/Webmap/network) [![GitHub stars](https://img.shields.io/github/stars/Kushal997-das/Webmap.svg)](https://github.com/kushal997-das/Webmap/stargazers)
![GitHub contributors](https://img.shields.io/github/contributors/googlemaps/google-maps-services-python)







Folium
-------
- Folium is a powerful Python library that helps you create several types of Leaflet maps. ... To get an idea, just zoom/click around on the next map to get an impression.<br> 

Documentation
----------------
https://python-visualization.github.io/folium/

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
### create a map object:
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


How to check the latitide and Longitude for any location:
---------------------------------------------------------
https://www.latlong.net/

<br>

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
print(m)
```
<br>
<img align='center' alt='png' width='370px' src="https://github.com/Kushal997-das/Webmap/blob/master/Images/outpu3.png"/> <br>

Code Links:
----------

<a href="https://github.com/Kushal997-das/Webmap/blob/master/map.py">View source code in (.py)</a><br>
<a href="https://github.com/Kushal997-das/Webmap/blob/master/map1.ipynb">View souce code in (.ipynb)</a><br>
<a href="https://github.com/Kushal997-das/Webmap/blob/master/map.html">View HTML file</a> <br>


Live Demo:
---------------

<img align='center' alt='png' width='370px' src="https://github.com/Kushal997-das/Webmap/blob/master/Images/gif.gif"/> <br>




LICENSE:
---------
Copyright (c) 2020 Kushal Das

This project is licensed under the MIT License









<p align="center">
  <b><i>Let's connect! Find me on the web.</i></b>

[<img height="30" src = "https://img.shields.io/badge/Youtube-%23E4405F.svg?&style=for-the-badge&logo=Youtube&logoColor=white">][Youtube] 
[<img height="30" src = "https://img.shields.io/badge/gmail-c14438?&style=for-the-badge&logo=gmail&logoColor=white">][gmail] 
[<img height="30" src="https://img.shields.io/badge/linkedin-blue.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />][LinkedIn]
[<img height="30" src="https://img.shields.io/badge/github-black.svg?&style=for-the-badge&logo=github&logoColor=white" />][Github]
<br />
<hr />

[youtube]: https://www.youtube.com/channel/UCIHj6mNCMnSnmWLHOxzIESw?view_as=subscriber
[gmail]: mailto:daskushal980@gmail.com
[linkedin]: https://www.linkedin.com/in/kushal-das-7337421a9/
[github]: https://github.com/Kushal997-das/



  
If you have any Queries or Suggestions, feel free to reach out to me.

<h3 align="center">Show some &nbsp;❤️&nbsp; by starring some of the repositories!</h3>


