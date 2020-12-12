import folium
#from PIL import Image

#ladakh = Image.open("ladakh.jpg")
#taj_mahel=Image.open('taj mahel.jpg')
#rammandir=Image.open('rammandir.jpg')




m = folium.Map(tiles='Stamen Toner', zoom_start=4)
iconSpiderman = folium.features.CustomIcon("ladakh.jpg", icon_size=(100,100))
iconHulk = folium.features.CustomIcon("taj mahel.jpg", icon_size=(100,100))
iconWolverine = folium.features.CustomIcon("rammandir.jpg", icon_size=(100,100))
folium.Marker([40.743720, -73.822030], tooltip="Ladakh", popup='Ladakh,India', icon=iconSpiderman).add_to(m)
folium.Marker([39.760979, -84.192200], tooltip="Taj Mahal", popup='Taj Mahal,India', icon=iconHulk).add_to(m)
folium.Marker([54.464180, -110.182259], tooltip="Ayodhya RamMandir", popup='Ayodhya RamMandir,India', icon=iconWolverine).add_to(m)
print(m)
m.save('map.html')