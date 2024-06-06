import geemap

print(geemap.__version__)

#Create an interactive map

m = geemap.Map(center=[20, 0], zoom=2, height='600px')
# Add basemap
m.add_basemap("CartoDB.DarkMatter")
# Add text to the map
text = "Davide Tita"
m.add_text(text, fontsize=10, position='bottomright')
# Add a logo to the map
logo = 'https://tse3.mm.bing.net/th?id=OIP.y_0RA3ahpjhJFSbyGXeaOQHaEH&pid=Api'
m.add_image(logo, position='bottomright', width='100px', height='80px')
# Add GeoJSON data to the map
cables = 'https://open.gishub.org/data/vector/cables.geojson'
callback = lambda feat: {"color": feat["properties"]["color"], "weight": 1}
m.add_geojson(cables, layer_name="Cable lines", style_callback=callback)
# Display the map
m







