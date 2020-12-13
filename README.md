|PyPI| |Travis| |Gitter| |DOI| |binder|

.. |PyPI| image:: https://img.shields.io/pypi/v/folium.svg
    :target: https://pypi.org/project/folium
    :alt: PyPI Package

.. |Travis| image:: https://travis-ci.org/python-visualization/folium.svg?branch=master
    :target: https://travis-ci.org/python-visualization/folium
    :alt: Travis Build Status

.. |Gitter| image:: https://badges.gitter.im/python-visualization/folium.svg
    :target: https://gitter.im/python-visualization/folium
    :alt: Gitter

.. |DOI| image:: https://zenodo.org/badge/18669/python-visualization/folium.svg
   :target: https://zenodo.org/badge/latestdoi/18669/python-visualization/folium
   :alt: DOI
   
.. |binder| image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/python-visualization/folium/master?filepath=examples

folium
======

|folium|

Python Data, Leaflet.js Maps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`folium` builds on the data wrangling strengths of the Python ecosystem and the
mapping strengths of the Leaflet.js library. Manipulate your data in Python, 
then visualize it in a Leaflet map via `folium`.

Installation
------------

.. code:: bash

    $ pip install folium

or

.. code:: bash

    $ conda install -c conda-forge folium

















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
