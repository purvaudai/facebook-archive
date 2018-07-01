#replace api key for GoogleV3 with valid api key

import matplotlib.pyplot as plt
import os
import timestring
import datetime
from datetime import timedelta
import dateutil.parser
import numpy as np
import json
from geopy.geocoders import GoogleV3
#import geopy.geocoders
from tabulate import tabulate

"""
Plot your location.
Author - @purvaudai
"""

today = datetime.datetime.now().strftime('%b %d, %y')
yesterday = (datetime.datetime.now() - timedelta(days=1)).strftime('%b %d, %y')

def locations_plot():
    loc = raw_input('Enter facebook archive extracted location: ')
    if not os.path.isdir(loc):
        print("The provided location doesn't seem to be right")
        exit(1)

    fname = loc + '/location_history/your_location_history.json'
    if not os.path.isfile(fname):
        print("The file your_location_history.json is not present at the entered location.")
        exit(1)

    with open(fname) as f:
        base_data = json.load(f)

    data = base_data['location_history']
    count = dict()
    count_key=[]
    count_value=[]
    locations=[]

    for ele in data:
        lat=ele['attachments'][0]['data'][0]['place']['coordinate']['latitude']
        long=ele['attachments'][0]['data'][0]['place']['coordinate']['longitude']
        lat=round(lat,3)
        long=round(long,3)
        location=(lat,long)
        locations.append(location)

    for loc in locations:
        count[loc]=count.get(loc,0)+1

    for item in count.items():
        a,b=item
        count_key.append(a)
        count_value.append(b)

    count_value, count_key=(list(t) for t in zip(*sorted(zip(count_value,count_key),reverse=True)))

    places = []
    i = 0

    new_count=dict()
    while len(places) <= 10:
        loc_name = location_name(count_key[i])
        i = i + 1
        loc_name = loc_name.split(", ")
        loc_name = loc_name[-4:-2]
        loc_name = (", ".join(loc_name))
        if (loc_name not in places):
            places.append(loc_name)
            new_count[loc_name]=count_value[i]
        else:
            new_count[loc_name]=new_count[loc_name]+count_value[i]

    place, frequency = zip(*new_count.items())
    frequency, place = (list(t) for t in zip(*sorted(zip(frequency, place), reverse=True)))

    #Plotting frequency v/s place for top 10 most visited places

    x=np.array([0,1,2,3,4,5,6,7,9,10,11])
    y=np.array(frequency)
    x_ticks=place
    plt.xticks(x, x_ticks,rotation=45, fontsize=8)
    plt.plot(x, y, linestyle='--', marker='o')
    plt.ylabel('Frequency')
    plt.title('Places frequently visited')
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    plt.show()

def location_name((lat,long)):
    lat=str(lat)
    long=str(long)
    pos=lat+", "+long
    geolocator=GoogleV3(api_key='AIzaSyCYfItqJg74fLscMQvdVCClab3gUrq0NRw')
    location=geolocator.reverse(pos,exactly_one=True)
    return location[0]

if __name__ == '__main__':
    locations_plot()