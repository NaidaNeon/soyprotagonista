from django import forms
from django.core.exceptions import ValidationError
from .models import *

class AddEmployee(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Не выбрано'

    class Meta:
        model = Admin_Panel
        fields = ['title', 'slug', 'occupation', 'cat', 'photo', 'login', 'password', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols':40, 'rows': 5})
        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if len(title) > 200:
                raise ValidationError('Длина превышает 200 символов')
            
            return title