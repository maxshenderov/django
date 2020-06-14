from django.shortcuts import render
from django.http import Http404

# Create your views here.


def MainView(request):
    return render(request, 'index.html')


def DepartureView(request, departure):
    departures = {"msk": "Из Москвы", "spb": "Из Петербурга", "nsk": "Из Новосибирска", "ekb": "Из Екатеринбурга",
                  "kazan": "Из Казани"}

    if not departures.get(departure):
        raise Http404
    return render(request, 'departure.html')


def TourView(request, id):
    return render(request, 'index.html')
