from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
menu = ['Статистика', 'Обучение', 'Настройки', 'О сайте/Контакты']

def index(request):
    posts = Admin_Panel.objects.all()
    return render(request, 'soytemplates/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def chats(request):
    return render(request, 'soytemplates/chats.html', {'menu': menu, 'title': 'Чаты'})  #функция для отобажения отдельной страницы Чаты 

def statistics(request):
    return render(request, 'soytemplates/statistics.html', {'menu': menu, 'title': 'Статистика'})  #функция для отобажения отдельной страницы Статистика 

def study(request):
    return render(request, 'soytemplates/study.html', {'menu': menu, 'title': 'Обучение'})  #функция для отобажения отдельной страницы Обучение 

def sets(request):
    return render(request, 'soytemplates/sets.html', {'menu': menu, 'title': 'Настройки'})  #функция для отобажения отдельной страницы Настройки 


# def study(request, study_id):       # с указанием ID обучения (1, 2, 3)
#     return HttpResponse(f"<h2>Обучение</h2><p>{study_id}</p>")

# def chat(request, chat_type):        # с указанием типа чата (HR, accountant)
#     return HttpResponse(f"<h2>Чаты</h2><p>{chat_type}</p>")

# def sets(request, set_type):
#     return HttpResponse(f"<h2>Настройки</h2><p>{set_type}</p>")

