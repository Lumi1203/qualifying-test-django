from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile
from django.contrib.auth import get_user_model


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'address', 'password1', 'password2']


User = get_user_model()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address']

class UpdateProfileForm(forms.ModelForm):
    password = None  # hide password field

    class Meta:
        model = Profile
        fields = ['photo']

