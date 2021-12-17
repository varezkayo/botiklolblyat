import overpyapi = overpy.Overpass()
r = api.query("""
area["ISO3166-1"="DE"][admin_level=2];  #пользователь должени сам ввести значение DE
(node["amenity"="cafe"](area);
 way["amenity"="cafe"](area);
 rel["amenity"="cafe"](area);
);
out center;
""")coords  = []
coords += [(float(node.lon), float(node.lat))
           for node in r.nodes]
coords += [(float(way.center_lon), float(way.center_lat))
           for way in r.ways]
coords += [(float(rel.center_lon), float(rel.center_lat))
           for rel in r.relations]
