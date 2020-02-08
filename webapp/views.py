from django.shortcuts import render
import requests
from .models import flight
from .serializers import flightSerializer


def index(request):
    return render(request,'index.html')

def flight_list(request):
    if request.method=='POST':
        des=request.POST.get('destination')
        ori=request.POST.get('origin')
        des.upper()
        ori.upper()

    import requests

    url = "https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v1/prices/cheap"

    querystring = {"destination": des, "origin": ori, "currency": "USD", "page": "None"}

    headers = {
        'x-rapidapi-host': "travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com",
        'x-rapidapi-key': "cee0235719msh626cdee9f75e1cep1d0247jsn858dcefff174",
        'x-access-token': "c5a6fa7f19ee3975cd18b55384d00626"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    r = response.json()

    s = (r['data'])

    for key, value in s.items():
        key_val=str(key)

    t = (r['data'][key_val])

    k = []
    airline = []
    departure = []
    returnT=[]
    price = []

    for key, value in t.items():
        #print(key, value['airline'], value['departure_at'], value['price'], value['return_at'])
        k += key
        airline.append(value['airline'])
        departure.append(value['departure_at'])
        price.append(value['price'])
        returnT.append(value['return_at'])

    airline_info = zip(k, airline, departure,returnT,price)

    params = {'airline_info': airline_info}

    return render(request,'flight-list-view.html',params)















