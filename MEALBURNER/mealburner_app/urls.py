from django.urls import path
from .views import index
#from . import views
urlpatterns = [
    # views.index
    path("", index, name="home")
]
