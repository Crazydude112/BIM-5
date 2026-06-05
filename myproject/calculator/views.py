from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import MathCalculate, Measurement
def calculate(request):
    m=MathCalculate()
    meas= Measurement()
    s= m.sum(5, 3)
    d= m.divide(10, 2)
    a= meas.area_of_circle(4)
    r= meas.area_of_rectangle(5, 3)
    result = f"Sum: {s}, Division: {d}, Area of Circle:{a}, Area of Rectangle: {r}"
    return HttpResponse(result)