from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from todo.models import CustomUser, Task

class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed']