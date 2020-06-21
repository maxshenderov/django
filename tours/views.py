from django.shortcuts import render
from django.http import Http404

import random

from tours.data import data


# Create your views here.


def MainView(request):
    context = {"rangeMax": random.sample(range(1, 16), 6)}
    return render(request, 'index.html', context=context)


def DepartureView(request, departure):
    departures = {"msk": "Из Москвы", "spb": "Из Петербурга", "nsk": "Из Новосибирска", "ekb": "Из Екатеринбурга",
                  "kazan": "Из Казани"}
    departuresFilter = []
    pricemin = 10000000000
    pricemax = 0
    nightsmin = 10000000000
    nightsmax = 0
    tourcount = 0
    for key, value in data(request)["tours"].items():
        if value["departure"] == departure:
            departuresFilter.append(key)
            pricemax = max(value["price"], pricemax)
            pricemin = min(value["price"], pricemin)
            nightsmax = max(value["nights"], nightsmax)
            nightsmin = min(value["nights"], nightsmin)
            tourcount = tourcount + 1
    if not departures.get(departure):
        raise Http404

    departurename = departures[departure]
    context = {"rangeMax": departuresFilter,
               "departure": departure,
               "departurename": departurename[0].lower() + departurename[1:len(departurename)],
               "pricemax": pricemax,
               "pricemin": pricemin,
               "nightsmax": nightsmax,
               "nightsmin": nightsmin,
               "tourcount": tourcount,
               }

    return render(request, 'departure.html', context)


def TourView(request, id):
    tour = data(request)["tours"][id]
    departure = data(request)["departures"][tour["departure"]]
    stars = ""
    i = 0
    while i < int(tour["stars"]):
        i = i + 1
        stars = stars + "★"
    context = {"tour": tour, "departure": departure[0].lower() + departure[1:len(departure)], id: id, "stars": stars}
    print(stars)
    return render(request, 'tour.html', context=context)
