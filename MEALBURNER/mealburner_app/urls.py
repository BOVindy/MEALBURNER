from django.urls import path
from .views import index, daily_view, create_meal, delete_meal, delete_activity, profile_create, update_meal, view_profile, create_activity, update_activity
#from . import views

urlpatterns = [
    path('', index, name='home'),
    path('view_meal', daily_view, name='view'),
    path('create_meal', create_meal, name='create_meal'),
    path('delete_meal', delete_meal, name='delete_meal'),
    path('create_activity', create_activity, name='create_activity'),
    path('delete_activity', delete_activity, name='delete_activity'),
    path('profile', profile_create, name='profile'),
    path('update_meal/<int:id>', update_meal, name='update_meal'),
    path('update_activity/<int:id>', update_activity, name='update_activity'),
    path('view_profile', view_profile, name='view_prof')
]
