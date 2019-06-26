from django.urls import path
from .views import index, daily_view, create_meal, delete, profile_create, update_meal, view_profile
#from . import views

urlpatterns = [
    path('', index, name='home'),
    path('view_meal', daily_view, name='view'),
    path('create_meal', create_meal, name='create'),
    path('delete_meal', delete, name='delete'),
    path('profile', profile_create, name='profile'),
    path('update', update_meal, name='update'),
    path('view_profile', view_profile, name='view_prof')
]
