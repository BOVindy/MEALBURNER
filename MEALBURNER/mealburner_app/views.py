from django.shortcuts import render

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

        new_meal = Meal():
        new_meals.food_name = request.POST["food_name"]
        new_meals.calories = request.POST["calories"]
        new_meals.meal_type = request.POST["meal_type"]
        new_meals.date = request.POST["date"]

        new_meal.save()

        return redirect("daily_meals")

    return render(request, "mealburner_app/create_meal.html")

def delete(request):

    if request.method == "POST":

        to_delete = Meal.objects.get(id=request.POST["id"])

        to_delete.delete()

        return redirect("daily_meals")

    return redirect("daily_meals")

def history_view(request):

    if request.method == "POST":

        for loop stuff

    return render(request, "home")

def profile_create(request):

    if request.method == "POST":

        new_profile = Profile():
        new_profile.username = request.POST["username"]
        new_profile.weight = request.POST["weight"]
        new_profile.height = request.POST["height"]
        new_profile.age = request.POST["age"]
        new_profile.activity_level = request.POST["activity_level"]