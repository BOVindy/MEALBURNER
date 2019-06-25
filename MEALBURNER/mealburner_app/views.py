from django.shortcuts import render

def index(request):
    return render(request, 'mealburner_app/home.html')
# Create your views here.
