from django.urls import path
from .views import index, daily_view, create_meal, delete_meal, delete_activity, profile_create, update_meal, view_profile, create_activity, update_activity, cal_box, index2, individual_act_view, individual_meal_view, pie_chart
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
    path('view_profile/<int:id>', view_profile, name='view_prof'),
    path('view_cal_plot', cal_box, name='view_cal'),
    path('about', index2, name='about'),
    path('individual_meal_view/<int:id>', individual_meal_view, name='individual_meal_view'),
    path('individual_act_view/<int:id>', individual_act_view,name='individual_act_view' ),
    path('pie_chart/<int:id>', pie_chart, name='pie_chart')

]
