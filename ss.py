from geopy.geocoders import GoogleV3
import json
geolocator = GoogleV3(api_key='AIzaSyCYfItqJg74fLscMQvdVCClab3gUrq0NRw')
location = geolocator.geocode("Washington", language='en')
if location != None:
    print json.dumps(location.raw, indent=4)
    print location.address
else:
    print "No location!" , location
location = geolocator.reverse("52.509669, 13.376294")
print(location.raw)