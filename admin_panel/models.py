from email.policy import default
from django.db import models
from django.urls import reverse
from django.forms import CharField

# Create your models here.

class Admin_Panel(models.Model):
    title = models.CharField(max_length = 255, verbose_name='Full name')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    occupation = models.CharField(max_length = 255)
    department = models.CharField(max_length = 255)
    login = models.CharField(max_length = 100)
    password = models.CharField(max_length = 36)
    content = models.TextField(blank=False)
    photo = models.ImageField(upload_to="soyphotos")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Department')

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('employee', kwargs={'employee_slug': self.slug})

    class Meta:
        verbose_name = 'List of employees'
        verbose_name_plural = 'List of employees'
        ordering = ['title']  

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name = 'CATEGORY')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
