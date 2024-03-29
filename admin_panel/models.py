from email.policy import default
from django.db import models
from django.urls import reverse
from django.forms import CharField

# Create your models here.

class Admin_Panel(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField(blank=False)
    photo = models.ImageField(upload_to="soyphotos")
    time_startlesson = models.DateTimeField(auto_now=True)
    is_registered = models.BooleanField(default=True)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'List of employees'
        verbose_name_plural = 'List of employees'
        ordering = ['title']   #['title', 'time_create']

# class Category