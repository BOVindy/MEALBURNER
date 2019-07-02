from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Meal, Profile, Activity
from datetime import datetime
import matplotlib.pyplot as plt


my_meals = Meal.objects.filter(profile=Project.objects.get(username=usr))
my_activities = Activity.objects.filter(profile=Profile.objects.get(username=usr))
date_list = []
print(my_meals)
for i in list(my_meals):
    print(i)


total = 0
total_cal = 0
total_cal_burned = 0

for meal in my_meals:
    total_cal += meal.calories
    
for activity in my_activities:
    total_cal_burned += activity.calories_burned
    
total = total_cal - total_cal_burn
cal_plot = plt.bar(date_list, total)



