from django.contrib import admin

# Register your models here.
from .models import *

class SoyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'occupation', 'department','photo', )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'occupation', 'department',)
    list_filter = ('department', 'occupation',)
    prepopulated_fields = {'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}
    
admin.site.register(Admin_Panel, SoyAdmin)
admin.site.register(Category, CategoryAdmin)