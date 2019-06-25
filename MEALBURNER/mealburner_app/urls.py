from django.urls import path
from .views import Index
#from . import views

urlpatterns = [
    # views.index
    path("", index, name="home")
]
