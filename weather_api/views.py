import requests
from django.conf import settings
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
from django.http import HttpResponseBadRequest
from django.contrib import messages
def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']

            # Check if the city already exists in the database
            if City.objects.filter(name__iexact=city_name).exists():
                messages.error(request, "City already exists")
            else:
                # Check if the city name is valid using the OpenWeatherMap API
                api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={settings.OPEN_WEATHER_API_KEY}&units=metric"
                response = requests.get(api_url)
                if response.status_code == 200:
                    form.save()
                    return redirect('index')
                else:
                    messages.error(request, "Invalid city name")
        else:
            messages.error(request, "Invalid input")
    else:
        form = CityForm()

    cities = City.objects.all()
    weather_data = []
    for city in cities:
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city.name}&appid={settings.OPEN_WEATHER_API_KEY}&units=metric"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            # Add error handling for missing keys
            try:
                temperature = data["main"]["temp"]
                description = data["weather"][0]["description"]
                weather_data.append({
                    "city": city.name,
                    "temperature": temperature,
                    "description": description,
                })
            except KeyError as e:
                print(f"KeyError: {e} for city {city.name}")
        else:
            print(f"Failed to fetch weather data for city {city.name}, status code: {response.status_code}")

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'index.html', context)


def reset_cities(request):
    City.objects.all().delete()
    return redirect('index')
