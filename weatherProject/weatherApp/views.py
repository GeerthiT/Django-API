# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import urllib.request
import json
import requests

# Create your views here.

def index(request):

    ip =  urllib.request.urlopen('https://api.ipify.org?format=json').read()
    ip_data = json.loads(ip)
    ip_addr = {
        "ip" : str(ip_data['ip'])
    }
    print(ip_addr)

    coord = requests.get('http://ip-api.com/json/' + ip_data["ip"])
    location_data = coord.text
    coord_data = json.loads(location_data)
    co_ord = {
        "lat" : str(coord_data['lat']),
        "lon" : str(coord_data['lon']),
    }
    print(co_ord)

    temp_source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?lat=' + str(coord_data["lat"]) + '&lon=' + str(coord_data["lon"]) + '&appid=08318ab7e98f0fc14a9ec4c556d11520&units=metric').read()

    data_list = json.loads(temp_source)

    data = {
            "country_code" : str(data_list['sys']['country']),
            "coordinate" : str(data_list['coord']['lon']) + ', ' +str(data_list['coord']['lat']),
            "temp" : str(data_list['main']['temp']) + 'C',
            "main": str(data_list['weather'][0]['main']),
            "description" : str(data_list['weather'][0]['description']),
            "icon" : str(data_list['weather'][0]['icon']),
        }
    
 ##   if request.method == 'POST':
 ##       city = request.POST['city']
 ##       source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=08318ab7e98f0fc14a9ec4c556d11520&units=metric').read()

 ##       data_list = json.loads(source)

 ##      data = {
 ##           "country_code" : str(data_list['sys']['country']),
 ##           "coordinate" : str(data_list['coord']['lon']) + ', ' +str(data_list['coord']['lat']),
 ##           "temp" : str(data_list['main']['temp']) + 'C',
 ##           "main": str(data_list['weather'][0]['main']),
 ##           "description" : str(data_list['weather'][0]['description']),
 ##           "icon" : str(data_list['weather'][0]['icon']),
 ##       }
 ##      print(data)

##    else:
 ##       data = {}

    return render(request, "main/index.html",data)