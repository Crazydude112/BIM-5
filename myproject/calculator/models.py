from django.db import models

# Create your models here.
from django.db import models
import math
class MathCalculate(models.Model):
    def sum(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
class Measurement(models.Model):
    def area_of_circle(self, radius):
        return math.pi * radius ** 2
    def area_of_rectangle(self, length, width):
        return length * width
    