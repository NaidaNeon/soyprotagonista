from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView

from .models import *
from .forms import *

# Create your views here.
head = [{'title': 'Добавить сотрудника', 'url_name':'add_employee'},
        {'title': 'Войти', 'url_name': 'login'}
        ]

# <!-- sidebar для меню суперюзера-hr -->
'''hr_menu = [
    {'title': 'Добавить сотрудника', 'url_name':'add_employee'}, 
    {'title': 'Отделы компании', 'url_name': 'category'},
    {'title': 'Список курсов', 'url_name': 'courses'},
]'''

menu = [{'title': 'Мои достижения', 'url_name': 'achievements'},
        {'title': 'Мои инструкции', 'url_name': 'instructions'},
        {'title': 'Мои задания', 'url_name': 'studies'},
        {'title': 'Настройки', 'url_name': 'sets'},
        {'title': 'Узнать больше', 'url_name': 'about'}
        ]

class AdminHome(ListView):
    model = Admin_Panel
    template_name = 'soytemplates/main.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['head'] = head
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0     #должна ссылка в боковом меню выделятьсЯ как текст
        return context

'''
def main(request):
    posts = Admin_Panel.objects.all()

    context = {
        'posts': posts, 
        'head': head,
        'menu': menu, 
        #'hr_menu': hr_menu,
        'cat_selected': 0, 
    }

    return render(request, 'soytemplates/main.html', context=context)
'''
def achievements(request):
    return render(request, 'soytemplates/achievements.html', {'menu': menu, 'title': 'Достижения'})  #функция для отобажения отдельной страницы Статистика 

def instructions(request):
    return render(request, 'soytemplates/instructions.html', {'menu': menu, 'title': 'Инструкции'})  #функция для отобажения отдельной страницы Статистика 

def studies(request):
    return render(request, 'soytemplates/studies.html', {'menu': menu, 'title': 'Задания'})  #функция для отобажения отдельной страницы Обучение 

def sets(request):
    return render(request, 'soytemplates/sets.html', {'menu': menu, 'title': 'Настройки'}) 

def about(request):
    return HttpResponse("Узнать больше")     #добавить отдельную страницу или так? //показать как работает

def addemployee(request):
    if request.method == 'POST':
        form = AddEmployee(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
    else:
        form = AddEmployee()
    return render(request, 'soytemplates/addemployee.html', {'form': form, 'menu': menu, 'title': 'Добавить нового сотрудника'})  #функция для отобажения страницы добавить сотрудника 

def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1><p>Попробуйте ввести запрос снова</p>')

def spisok(request, employee_slug):
    post = get_object_or_404(Admin_Panel, slug=employee_slug)
    context = {
        'post': post, 
        'head': head,   
        'menu': menu, 
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'soytemplates/post.html', context=context)

def show_category(request, cat_id):
    posts = Admin_Panel.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        return HttpResponseNotFound('<h1>Страница не найдена</h1><p>Попробуйте ввести запрос снова</p>')

    context = {
        'posts': posts, 
        'head': head,
        'menu': menu, 
        'title': 'Виды обучения',
        'cat_selected': cat_id, 
    }

    return render(request, 'soytemplates/main.html', context=context)
