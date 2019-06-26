from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from .models import Meal, Profile



def index(request):
    return render(request, 'mealburner_app/home.html')

def daily_view(request):

    my_meals = Meal.objects.all()

    context = {
        "daily_meals": my_meals
    }
    print(my_meals)

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

def delete(request):

    if request.method == "POST":

        to_delete = Meal.objects.get(id=request.POST["id"])

        to_delete.delete()

        return redirect("daily_meals")

        


    return render(request, "home")

def update_meal(request):
    if request.method == 'POST':
        meal = Meal.objects.get(id=request.POST.get('id'))
        meal.food_name = request.POST['food_name']
        meal.food_calories = request.POST['calories']
        meal.meal_type = request.POST['meal_type']
        meal.date = request.POST['date']
        meal.save()

        return redirect('daily_meals')
    
    return render(request, 'mealburner_app/create_meal.html')
        
        

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
        
        return redirect('profile')
    
    return render(request, 'mealburner_app/create_profile.html')

def view_profile(request):

    my_profile = Profile.objects.all()

    context = {
        'profile' : my_profile
    }

    print(my_profile)

    return render(request, 'mealburner_app/profile_view.html', context=context)


