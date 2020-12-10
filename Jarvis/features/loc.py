import webbrowser
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import geocoder

def loc(place):
    # webbrowser.open("http://www.google.com/maps/place/" + location + "")
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(place)
    print(location.address)
    target_latlng = location.latitude, location.longitude
    print(target_latlng)
    current_loc = geocoder.ip('me')
    current_latlng = current_loc.latlng
    distance = great_circle(current_latlng, target_latlng)
    print(distance)
    return current_loc, distance

loc('Mumbai')