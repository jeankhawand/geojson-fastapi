from models.GeoJson import GeoJson
from models.ISOCodeRequest import ISOCodeRequest
import folium


def return_iso_code(request: ISOCodeRequest, geojson: GeoJson):
    if len(request.countries) > 5 and request.detail:
        print("[OPERATION] = countries length > 5 and detail is enabled")
        return geojson.return_countries_with_iso_code(request.countries, request.detail)
    if len(request.countries) > 5:
        print("[OPERATION] = countries length > 5 and detail is disabled")
        return geojson.return_countries_with_iso_code(request.countries)
    if 5 >= len(request.countries) > 0 and request.detail:
        print("[OPERATION] =  0 < countries length <= 5 and detail is enabled")
        return geojson.return_countries_with_iso_code(request.countries, request.detail)
    if 5 >= len(request.countries) > 0:
        print("[OPERATION] =  0 < countries length <= 5 and detail is disabled")
        return geojson.return_countries_with_iso_code(request.countries)


def return_countries_list(geojson: GeoJson):
    countries_list = []
    for feature in geojson.features:
        countries_list.append(feature.properties.name)
    return countries_list


def generate_all_geometrics(geojson: GeoJson):
    m = folium.Map(location=[0, 0], zoom_start=2)
    folium.GeoJson(data=geojson.json(), style_function=style_function).add_to(m)
    m.save("static/map.html")
    return True


def style_function(feature):
    return {
        "fillOpacity": 0.5,
        "weight": 0,
        "fillColor": "#ff1a1a",
    }
