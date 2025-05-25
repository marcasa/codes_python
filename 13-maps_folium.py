import folium

mapa = folium.Map(location=[-23.504739091623104, -46.47615680521386], zoom_start=50)

#inserindo marcadores

locais = [
    {"localização": [-23.499396981785367, -46.47852459164998 ], "nome": " E.E. Therezinha"},
    {"localização": [ -23.50552608179492, -46.476837876463364], "nome": " Cido Cabelereiro "},
    {"localização": [-23.50579646102427, -46.476639861826236 ], "nome": " Adega dos noias "}
]


for local in locais:
    folium.Marker(
        location=local["localização"],
        popup=local["nome"],
        icon=folium.Icon(color='green', icon='info-sign')

    ).add_to(mapa)

mapa.save('mapa.html')