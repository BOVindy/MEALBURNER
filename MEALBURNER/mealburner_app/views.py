from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Meal, Profile, Activity
from datetime import datetime
import matplotlib.pyplot as plt



def index(request):
    return render(request, 'mealburner_app/home.html')

def index2(request):
    return render(request, 'mealburner_app/about.html')

def daily_view(request):
    usr = request.user
    usrs_food = Meal.objects.filter(profile=Profile.objects.get(username=usr))
    usr_stats = Profile.objects.filter(username=request.user)
    # my_activities = Activity.objects.filter(username=request.user)
    usr_act = Activity.objects.filter(profile=Profile.objects.get(username=usr))

    total = 0
    total_cal = 0
    total_cal_burn = 0

    for meal in usrs_food:
        total_cal += meal.calories

    for activity in usr_act:
        total_cal_burn += activity.calories_burned

    total = total_cal - total_cal_burn

    total_protein = 0
    total_carbs = 0
    total_fats = 0
    
    for meal in usrs_food:
        total_protein += meal.protein
    
    for meal in usrs_food:
        total_carbs += meal.carbohydrates
    
    for meal in usrs_food:
        total_fats += meal.fats

    for profile in usr_stats:
        user_weight = profile.weight


    recommended_protein = int(user_weight) * .8
    
    recommended_carb = int(user_weight) * .5

    recommended_fat = int(user_weight) * .27

    context = {
        "daily_meals": usrs_food,
        "daily_activities": usr_act,
        "total": total,
        "daily_cal": total_cal,
        "daily_cal_burn": total_cal_burn,
        "daily_protein" : total_protein,
        "daily_carbs" : total_carbs,
        "daily_fats" : total_fats,
        "recommended_protein" : recommended_protein,
        "recommended_carbs" : recommended_carb,
        "recommended_fat" : recommended_fat
    }
#    print(my_meals)
#    print(my_activities)

    return render(request, "mealburner_app/daily_meals.html", context=context)


def create_meal(request):

    if request.method == "POST":

        usr = request.user
        new_meal = Meal()

        new_meal.profile = Profile.objects.get(username=usr)

        new_meal.food_name = request.POST["food_name"]
        new_meal.calories = request.POST["calories"]
        new_meal.meal_type = request.POST["meal_type"]
        new_meal.protein = request.POST["protein"]
        new_meal.carbohydrates = request.POST["carbohydrates"]
        new_meal.fats = request.POST["fats"]
        new_meal.date = request.POST["date"]

        new_meal.save()

        return redirect("view")

    return render(request, "mealburner_app/create_meal.html")
#added date to here, need to work on it

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
        new_profile.username = request.POST["username"]
        new_profile.firstname = request.POST['firstname']
        new_profile.lastname = request.POST['lastname']
        new_profile.weight = request.POST["weight"]
        new_profile.height = request.POST["height"]
        new_profile.age = request.POST["age"]
        new_profile.activity_level = request.POST["activity_level"]
        new_profile.calorie_intake_goal = float(request.POST["calorie_intake_goal"])
        new_profile.calorie_output_goal = float(request.POST["calorie_output_goal"])
        new_profile.regular_exercises = request.POST["activity_level"]
        new_profile.fitness_goal = request.POST['fitness_goal']
        new_profile.password = request.POST['password']
        
        new_profile.save()
        user = User.objects.create_user(username=new_profile.username, password=new_profile.password)
        user.save()
        
        return redirect('http://127.0.0.1:8000/')
        
        
    return render(request, 'mealburner_app/create_profile.html')

def view_profile(request, id):

    usr = User.objects.get(id=id)
    print(usr)
    all_profile = Profile.objects.filter(username=request.user)
    print(all_profile)
    for p in all_profile:
        print(p.firstname)
        if p.username == usr.username:
            my_profile = p
            break
    else:
        print("Didn't Work")
        my_profile = ""

    context = {
        'profile' : my_profile
    }

    print(my_profile)

    return render(request, 'mealburner_app/profile_view.html', context=context)


#################################################################

def create_activity(request):

    if request.method == "POST":
        usr = request.user
        new_activity = Activity()

        new_activity.profile = Profile.objects.get(username=usr)

        
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

def cal_box(request):
    usr = request.user

    my_meals = Meal.objects.filter(profile=Profile.objects.get(username=usr))
    
    my_activities = Activity.objects.filter(profile=Profile.objects.get(username=usr))
    
    new_list = []
    for i in my_meals:
        new_list.append(i.date.strftime('%m/%d/%Y')) 
         
    print(new_list)
    
    total = 0

    total_cal = 0

    total_cal_burn = 0

    for meal in my_meals:
        total_cal += meal.calories
    
    for activity in my_activities:
        total_cal_burn += activity.calories_burned
    
    total = total_cal - total_cal_burn
    
    cal_plot = plt.bar(new_list, total, color='#688087', linewidth=0)
    
    my_path = "/Users/jschmidt/Desktop/pythonbootcam/projects/MEALBURNER/MEALBURNER/mealburner_app/static/mealburner_app/graphs"
    
    plt.xlabel('Date')
    plt.ylabel('Total Calories')
    plt.title('Total Calories Consumed Per Day')
    plt.savefig(my_path+'/cal_plot.png')
    

    return render(request, 'mealburner_app/plots.html')

