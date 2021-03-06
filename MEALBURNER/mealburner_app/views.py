from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Meal, Profile, Activity
from datetime import datetime
import matplotlib.pyplot as plt
import os



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
    if total_protein < recommended_protein:
        protein_needed = int(recommended_protein) - int(total_protein)
    else:
        protein_needed = 0

    if total_carbs < recommended_carb:
        carbs_needed = int(recommended_carb) - int(total_carbs)
    else: 
        carbs_needed = 0

    if total_fats < recommended_fat:
        fats_needed = int(recommended_fat) - int(total_fats)
    else:
        fats_needed = 0

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
        "recommended_fat" : recommended_fat,
        "protein_needed" : protein_needed, 
        "carbs_needed" : carbs_needed,
        "fats_needed" : fats_needed
    }


    return render(request, "mealburner_app/daily_meals2.html", context=context)


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
        new_profile.regular_exercises = request.POST["regular_exercises"]
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
        new_activity.date = request.POST["date"]
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
    
    date_list = [x.strftime('%m/%d/%Y') for x in sorted({i.date for i in my_meals})]
    cal_list = []

    for x in date_list:
        total_cal = 0
        total_cal_burn = 0
        for m in my_meals:
            if m.date.strftime('%m/%d/%Y') == x:
                total_cal += m.calories
        for a in my_activities:
            if a.date.strftime('%m/%d/%Y') == x:
                total_cal_burn += a.calories_burned

        cal_list.append(total_cal - total_cal_burn)
    
    cal_plot = plt.bar(date_list, cal_list, color='#688087', linewidth=0)
    
    plt.xlabel('Date')
    plt.ylabel('Total Calories')
    plt.title('Total Calories Consumed Per Day')
    plt.savefig(os.getcwd() + '/mealburner_app/static/mealburner_app/graphs/cal_plot.png')
    plt.close()

    return render(request, 'mealburner_app/plots.html')

def individual_meal_view(request, id):
    usr = request.user
    
    usrs_food = Meal.objects.filter(profile=Profile.objects.get(username=usr))
    
    usr_stats = Profile.objects.filter(username=request.user)
    
    meal_to_view = Meal.objects.get(id=id)

    m_d = Meal.objects.filter(date=meal_to_view.date)

    total_protein = 0
    total_carbs = 0
    total_fats = 0
    
    for meal in m_d:
        total_protein += meal.protein
    
    for meal in m_d:
        total_carbs += meal.carbohydrates
    
    for meal in m_d:
        total_fats += meal.fats

    for profile in usr_stats:
        user_weight = profile.weight


    recommended_protein = int(user_weight) * .8
    
    recommended_carb = int(user_weight) * .5

    recommended_fat = int(user_weight) * .27
    
    if total_protein < recommended_protein:
        protein_needed = int(recommended_protein) - int(total_protein)
    else:
        protein_needed = 0

    if total_carbs < recommended_carb:
        carbs_needed = int(recommended_carb) - int(total_carbs)
    else: 
        carbs_needed = 0

    if total_fats < recommended_fat:
        fats_needed = int(recommended_fat) - int(total_fats)
    else:
        fats_needed = 0
    
    

    context = {
        'meal' : m_d,
        "daily_protein" : total_protein,
        "daily_carbs" : total_carbs,
        "daily_fats" : total_fats,
        "recommended_protein" : recommended_protein,
        "recommended_carbs" : recommended_carb,
        "recommended_fat" : recommended_fat,
        "protein_needed" : protein_needed, 
        "carbs_needed" : carbs_needed,
        "fats_needed" : fats_needed
    }

    return render(request, 'mealburner_app/meal_act_view.html', context=context)

def individual_act_view(request, id):
    
    activity_to_view = Activity.objects.get(id=id)

    a_d = Activity.objects.filter(date=activity_to_view.date)

    context = {
        'activity' : a_d
    }

    return render(request, 'mealburner_app/meal_act_view.html', context=context)

def pie_chart(request, id):
    usr = request.user

    usrs_food = Meal.objects.filter(profile=Profile.objects.get(username=usr))
    
    usr_stats = Profile.objects.filter(username=request.user)
    
    meal_to_view = Meal.objects.get(id=id)

    m_d = Meal.objects.filter(date=meal_to_view.date)

    total_protein = 0
    total_carbs = 0
    total_fats = 0
    
    for meal in m_d:
        total_protein += meal.protein
    
    for meal in m_d:
        total_carbs += meal.carbohydrates
    
    for meal in m_d:
        total_fats += meal.fats
         
    context = {
        'meal' : m_d,
        'daily_protein' : total_protein,
        'daily_carbs' : total_carbs,
        'daily_fats' : total_fats
    }
    nutrient_list = [int(total_protein), int(total_carbs), int(total_fats)]
    print(nutrient_list)
    
    sizes = [15, 30, 45, 10]
    explode = (0.1, 0.1, 0.1)
    labels = ['protein', 'carbs', 'fats']

    pie_chart = plt.pie(nutrient_list, explode=explode, labels= labels, shadow=True, autopct='%1.1f%%')
    print(os.getcwd())
    plt.title('Nutritional Breakdown')
    plt.savefig(os.getcwd() + '/mealburner_app/static/mealburner_app/graphs/pie_chart.png')
    plt.close()


    return render(request, 'mealburner_app/plots2.html')

