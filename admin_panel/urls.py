from django.urls import path

from .views import *

urlpatterns = [
    path('', AdminHome.as_view(), name='home'), #http://127.0.0.1:8000/

    #path('', main, name='home'), #http://127.0.0.1:8000/
    path('achievements/', achievements, name='achievements'), #http://127.0.0.1:8000/achievements/
    path('instructions/', instructions, name='instructions'),  #http://127.0.0.1:8000/instructions/
    path('studies/', studies, name='studies'), #http://127.0.0.1:8000/studies/
    path('sets/', sets, name='sets'), #http://127.0.0.1:8000/sets/
    path('login/', login, name='login'),
    path('addemployee/', addemployee, name='add_employee'),
    path('about/', about, name='about'),
    path('employee/<slug:employee_slug>/', spisok, name='employee'), #go to certain employee or course
    path('category/<int:cat_id>/', show_category, name='category'), #go to certain category of departments

]
