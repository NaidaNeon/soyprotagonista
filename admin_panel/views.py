from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'Статистика', 'url_name': 'statistics'},
        {'title': 'Обучение', 'url_name': 'studies'},
        {'title': 'Настройки', 'url_name': 'sets'},
        {'title': 'О сайте/Контакты', 'url_name': 'about'},
        {'title': 'Войти', 'url_name': 'login'}
        ]

def main(request):
    posts = Admin_Panel.objects.all()
    context = {
        'posts': posts, 
        'menu': menu, 
        'title': 'Главная страница'
    }

    return render(request, 'soytemplates/main.html', context=context)

def chats(request):
    return render(request, 'soytemplates/chats.html', {'menu': menu, 'title': 'Чаты'})  #функция для отобажения отдельной страницы Чаты 

def statistics(request):
    return render(request, 'soytemplates/statistics.html', {'menu': menu, 'title': 'Статистика'})  #функция для отобажения отдельной страницы Статистика 

def study(request):
    return render(request, 'soytemplates/study.html', {'menu': menu, 'title': 'Обучение'})  #функция для отобажения отдельной страницы Обучение 

def sets(request):
    return render(request, 'soytemplates/sets.html', {'menu': menu, 'title': 'Настройки'}) 

def about(request):
    return HttpResponse("О сайте/Контакты")     #добавить отдельную страницу или так? //показать как работает

def login(request):
    return HttpResponse("Авторизация")



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1><p>Попробуйте ввести запрос снова</p>')

def spisok(request, employee_id):
    return HttpResponse(f"Список сотрудников c id = {employee_id} и информация о них или же список курсов c id = {employee_id}")