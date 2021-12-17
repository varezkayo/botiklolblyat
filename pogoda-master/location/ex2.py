YOUR_API_KEY = 'API_KEY'
google_places = GooglePlaces(YOUR_API_KEY)

query_result = google_places.nearby_search(
        lat_lng={'lat': 52.0737017, 'lng': 5.0944107999999915}, #пользователь должен сам ввести lat и lng 
        radius=100,
        types=[types.TYPE_RESTAURANT] or [types.TYPE_CAFE])

for place in query_result.places:
     place.get_details()
     print '%s %s %s' % (place.name, place.geo_location, place.types)
