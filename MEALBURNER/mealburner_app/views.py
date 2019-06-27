from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from .models import Meal, Profile, Activity
from datetime import datetime



def index(request):
    return render(request, 'mealburner_app/home.html')

def daily_view(request):

    my_meals = Meal.objects.all()
    my_activities = Activity.objects.all()

    context = {
        "daily_meals": my_meals,
        "daily_activities": my_activities
    }
    print(my_meals)
    print(my_activities)

    return render(request, "mealburner_app/daily_meals.html", context=context)


def create_meal(request):

    if request.method == "POST":

        new_meal = Meal()
        new_meal.food_name = request.POST["food_name"]
        new_meal.calories = request.POST["calories"]
        new_meal.meal_type = request.POST["meal_type"]

        new_meal.save()

        return redirect("view")

    return render(request, "mealburner_app/create_meal.html")


def delete_meal(request):

    if request.method == "POST":
        print(request.POST['id'])
        to_delete = Meal.objects.get(id=request.POST["id"])

        to_delete.delete()

        return redirect("view")

    return render(request, "home")


def update_meal(request, id):

    meal_update = Meal.objects.get(id=id)

    if request.method == 'POST':
        print('updatemealexists')
        for key, value in request.POST.items():
            if(value and key != "csrfmiddlewaretoken"):
                setattr(meal_update, key, value)
        meal_update.save()

        return redirect('view')

    context = {
        "meal": meal_update
    }    

    return render(request, 'mealburner_app/update_meal.html', context=context)
        
        

def profile_create(request):

    if request.method == "POST":

        new_profile = Profile()
        new_profile.user = request.POST["username"]
        new_profile.firstname = request.POST['firstname']
        new_profile.lastname = request.POST['lastname']
        new_profile.weight = request.POST["weight"]
        new_profile.height = request.POST["height"]
        new_profile.age = request.POST["age"]
        new_profile.activity_level = request.POST["activity_level"]
        new_profile.password = request.POST['password']
        
        
        user = User.objects.create_user(username=new_profile.user, password=new_profile.password)
        user.save()
        
        return redirect('profile')
    
    return render(request, 'mealburner_app/create_profile.html')

def view_profile(request):

    my_profile = Profile.objects.all()

    context = {
        'profile' : my_profile
    }

    print(my_profile)

    return render(request, 'mealburner_app/profile_view.html', context=context)


#################################################################

def create_activity(request):

    if request.method == "POST":

        new_activity = Activity()
        new_activity.activity = request.POST["activity"]
        new_activity.duration = request.POST["duration"]
        new_activity.calories_burned = request.POST["calories_burned"]

        new_activity.save()

        return redirect("view")

    return render(request, "mealburner_app/create_activity.html")


def delete_activity(request):

    if request.method == "POST":
        print(request.POST['id'])
        to_delete = Activity.objects.get(id=request.POST["id"])

        to_delete.delete()

        return redirect("view")

    return render(request, "home")


def update_activity(request, id):

    activity_update = Activity.objects.get(id=id)

    if request.method == 'POST':
        print('updateactivityexists')
        for key, value in request.POST.items():
            if(value and key != "csrfmiddlewaretoken"):
                setattr(activity_update, key, value)
        activity_update.save()

        return redirect('view')

    context = {
        "activity": activity_update
    }    

    return render(request, 'mealburner_app/update_activity.html', context=context)




