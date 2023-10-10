from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name']
class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('full_name',)