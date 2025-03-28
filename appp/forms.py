from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    confim_password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
            'gender': forms.RadioSelect(choices=[('M', 'Male'), ('F', 'Female')]),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Select your birth date'})
        }
