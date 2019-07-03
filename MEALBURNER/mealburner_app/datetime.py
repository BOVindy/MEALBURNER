"""
day_previous = [0, 0]
day_current = [0, 0]
day_id = 0
daily_history = {
    day_id: usr_year, usr_day
}


def date_indexing(request):
    if date.day == day_previous[1] + 1:
        then day_current[1] += 1
        daily_history[1] += 1
        if date.day == day_previous[1] + 2:
        day_previous[1] += 1

    elif date.day == 1:
        day_current[1] = 1 #for days
        day_current[0] += 1 #for months
        daily_history[1] += 1
        if date.day == day_previous[1] + 2:
        day_previous[1] += 1


daily_history[day_id] = usr_year, usr_day
"""
"""
MD = {}

for m in meals:
    if m.date in MD.keys():
        MD[m.date].append(m)
    else:
        MD.update(m.date:[m])

wanting to have an id:
    each id will have a year and a day(1-366)

class Oftime:
    takes in an id and a date.
    stores those values.
    each new one instance will have a new id
    dates can't be repeated

store each instance of Oftime and add them to an indexable list

use the list of instances to find a particular saved date

each daily meals will be a sub-of the Oftime, multiple and unlimited meals allowed until day rolls over

foreign keys probable
struggle-definite
headaches-likely
"""
"""
date_id = 0

class Timedate:
    def __init__(self, day, month, year):
        global date_id
        date_id += 1
        self.tday = day
        self.tmonth = month
        self.tyear = year
        self.time_id = date_id

    def __repr__(self):
        return f"{self.time_id} {self.tday} {self.tmonth} {self.tyear}"

class Timehist:
    def __init__(self):
        self.timehist_list = []

    def get_timehist(self):
        return self.timehist_list

    def create_timedate(self, day, month, year):
        new_timedate = Timedate(day, month, year)
        self.timehist_list.append(new_timedate)




my_timehist = Timehist()
my_timehist_list = my_timehist.get_timehist()
for entry in my_timehist_list:

""""""
if day = day then do some code.(self, *args, **kwargs):
    return super().(*args, **kwargs)

for target_date in date_list:
    async for meal in day and for activity in day:
        return [{self.*meals}, {self.*activities}]

###########################################################3
def daily_view(request):

    my_meals = Meal.objects.filter(date)
    my_activities = Activity.objects.filter(date)

    total = 0
    total_cal = 0
    total_cal_burn = 0

    for meal in my_meals:
        total_cal += meal.calories

    for activity in my_activities:
        total_cal_burn += activity.calories_burned

    total = total_cal - total_cal_burn

    context = {
        "daily_meals": my_meals,
        "daily_activities": my_activities,
        "total": total,
        "daily_cal": total_cal,
        "daily_cal_burn": total_cal_burn

    }
#    print(my_meals)
#    print(my_activities)

    return render(request, "mealburner_app/daily_meals.html", context=context)
"""
"""
###################################################################################
def daily_view(request):
    usr = request.user



    usrs_food = Meal.objects.filter(profile=Profile.objects.get(username=usr))
    
    # my_activities = Activity.objects.filter(username=request.user)
    usr_act = Activity.objects.filter(profile=Profile.objects.get(username=usr))

    total = 0
    total_cal = 0
    total_cal_burn = 0

    for m in usrs_food:
        print(m.date)
"""
##################################################################################33

m_date_all = meal.date.split()
a_date_all = activity.date.split()

usrs_food = Meal.objects.filter(profile=Profile.objects.get(username=usr), m_date_all[2])
    

usr_act = Activity.objects.filter(profile=Profile.objects.get(username=usr), a_date_all[2])

##########################################################################################
    for meal in usrs_food:
        m_date_all = meal.date.split()
        if:
            x == m_date_all[2]
            pass
        else:
            x = m_date_all[2]
            append something

    for activity in usrs_act:
        a_date_all = activity.date.split()
        if:
            y == a_date_all[2]
            pass
        else:
            y = a_date_all[2]
            append something


##############################################################################################33333
"""
    for meal in usrs_food:
        total_cal += meal.calories

    for activity in usr_act:
        total_cal_burn += activity.calories_burned

    total = total_cal - total_cal_burn

    # # now = Meal.datetime()
    # year = now.strftime("%Y")
    # month = now.strftime("%m")
    # day = now.strftime("%d")

    context = {
        "daily_meals": usrs_food,
        "daily_activities": usr_act,
        "total": total,
        "daily_cal": total_cal,
        "daily_cal_burn": total_cal_burn

    }
#    print(my_meals)
#    print(my_activities)

    return render(request, "mealburner_app/daily_meals.html", context=context)

"""    ##############################################333
    new_list = []
    for i in my_meals:
        new_list.append(i.date.strftime('%m/%d/%Y %H:%M:%S')) 
