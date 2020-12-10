import webbrowser
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import geocoder

def loc(place):
    # webbrowser.open("http://www.google.com/maps/place/" + location + "")
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(place, addressdetails=True)
    target_latlng = location.latitude, location.longitude
    location = location.raw['address']
    target_loc = {'city': location.get('city', ''),
                   'state': location.get('state', ''),
                   'country': location.get('country', '')}
    current_loc = geocoder.ip('me')
    current_latlng = current_loc.latlng
    distance = great_circle(current_latlng, target_latlng)
    return current_loc, target_loc, distance

