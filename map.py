import folium
m = folium.Map(tiles='Stamen Toner', zoom_start=4)
ladakh = folium.features.CustomIcon("ladakh.jpg", icon_size=(100,100))
taj_mahhel = folium.features.CustomIcon("taj mahel.jpg", icon_size=(100,100))
rammandir= folium.features.CustomIcon("rammandir.jpg", icon_size=(100, 100))
folium.Marker([40.743720, -73.822030], tooltip="Ladakh", popup='Ladakh,India', icon=ladakh).add_to(m)
folium.Marker([39.760979, -84.192200], tooltip="Taj Mahal", popup='Taj Mahal,India', icon=taj_mahhel).add_to(m)
folium.Marker([54.464180, -110.182259], tooltip="Ayodhya RamMandir", popup='Ayodhya RamMandir,India', icon=rammandir).add_to(m)
print(m)
m.save('map.html')