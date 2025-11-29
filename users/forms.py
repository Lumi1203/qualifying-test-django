from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile
from django.contrib.auth import get_user_model


User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(
        choices=User.SELECT_ROLE,
        widget= forms.Select(attrs={'class': 'form-select'})
    )
    examiner_id = forms.CharField(
        required=False,
        widget= forms.TextInput(attrs= {'placeholder' : 'Enter Examiner Number'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'examiner_id', 'phone', 'address', 'password1', 'password2']

    def clean(self):
        cleaned = super().clean()
        role = cleaned.get("role")
        examiner_id = cleaned.get("examiner_id")

        if role == "examiner" and not examiner_id:
            self.add_error("examiner_id", "Examiner ID is required for examiners.")

        return cleaned


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address']

class UpdateProfileForm(forms.ModelForm):
    password = None 
    
    class Meta:
        model = Profile
        fields = ['photo']

