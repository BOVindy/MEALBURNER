from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser
from datetime import datetime

class Meal(models.Model):
    food_name = models.CharField(max_length=30)
    calories = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=30)
    date = models.DateTimeField(default=datetime.now, blank=True)


class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=30, decimal_places=2)
    age = models.DecimalField(max_digits=2, decimal_places=0)
    activity_level = models.CharField(max_length=30)


    
  

# Authentication in Web requests

# The login_required decorator
