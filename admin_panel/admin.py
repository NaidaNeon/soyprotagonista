from django.contrib import admin

# Register your models here.
from .models import *

# class Admin_Panel_Admin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'time_create', 'photo', 'is_registered')
#     list_display_links = ('id', 'title')
#     search_fields = ('title', 'content')

admin.site.register(Admin_Panel) #(Admin_Panel, Admin_Panel_Admin)