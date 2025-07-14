from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from todo.models import CustomUser, Task, Profile

class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']