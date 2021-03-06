from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser
from datetime import datetime



class Profile(models.Model):
    username = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=30, decimal_places=2)
    age = models.DecimalField(max_digits=2, decimal_places=0)
    activity_level = models.CharField(max_length=30)
    calorie_intake_goal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    calorie_output_goal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    regular_exercises = models.CharField(max_length=30)
    fitness_goal = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.username}'s profile"

class Meal(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=30)
    calories = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=30)
    protein = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    carbohydrates = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fats = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f"{self.profile}'s meal'"
# default for date could be datetime now, and users could enter in a date of their own
class Activity(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    activity = models.CharField(max_length=80)
    duration = models.IntegerField()#max value soon
    calories_burned = models.IntegerField()
    
    def __str__(self):
        return f"{self.profile}'s activty'"

# Authentication in Web requests

# The login_required decorator
# user = models.ForeignKey(User, on_delete=models.CASCADE)