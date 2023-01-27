from django.urls import path

from .views import *

urlpatterns = [
    path('', main, name='home'), #http://127.0.0.1:8000/
    path('chats/', chats, name='chats'), #http://127.0.0.1:8000/chats/
    path('statistics/', statistics, name='statistics'),  #http://127.0.0.1:8000/statistics/
    path('studies/', study, name='studies'), #http://127.0.0.1:8000/studies/
    path('sets/', sets, name='sets'), #http://127.0.0.1:8000/sets/
    path('login/', login, name='login'),
    path('about/', about, name='about'),
    path('employee/<int:employee_id>/', spisok, name='employee'), #go to certain employee or course
    path('category/<int:cat_id>/', show_category, name='category'), #go to certain employee or course

]
