from django.shortcuts import render
from django.http import HttpResponse
from .models import CarPost


class Car:  # Note that parens are optional if not inheriting from another class
    def __init__(self, manufacturer, year, carModel, color, body, isAvailable):
        self.manufacturer = manufacturer
        self.year = year
        self.carModel = carModel
        self.color = color
        self.body = body

cars = [
    Car('Ford', '2011', 'F150', 'Grey', 'Crew Cab', True),
    Car('Toyota', '2016', 'Tundra', 'Cobalt', 'Super Cab', True),
    Car('Mercedes', '2017', 'S-Class', 'Blue',  'Coupe', False)
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# route for cars index
def cars_index(request):
    cars = CarPost.objects.all()
    return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
    car = CarPost.objects.get(id=car_id)
    return render(request, 'cars/detail.html', { 'car': car })