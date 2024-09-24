from django.shortcuts import render
import requests

'''def home(request):
    weather_data = {}
    if request.method == 'POST':
        city = request.POST['city']
        API_KEY = 'bb0fd32a3dcf9b68b4d96e62af87cdc9' 
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric' 
        

        response = requests.get(url)
        if response.status_code ==200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'city not found'}

    return render(request, 'home.html',{'weather_data': weather_data})'''

def get_weather_data(city):
    API_KEY = 'bb0fd32a3dcf9b68b4d96e62af87cdc9' 
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric'  
    response = requests.get(url)
    return response.json()

def weather_view(request):
    weather_data = {}
    if request.method == 'POST':
        city_name = request.POST.get('city')
        if city_name:
            weather_data = get_weather_data(city_name)
            if weather_data.get('cod') != 200: 
                weather_data = {'error': 'Enter a proper city name'}
        else:
            weather_data = {'error': 'City name cannot be empty'}
    return render(request, 'home.html', {'weather_data': weather_data})

            




