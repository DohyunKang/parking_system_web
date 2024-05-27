from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    first_name = forms.CharField(label="이름", max_length=30)
    last_name = forms.CharField(label="성", max_length=30)
    car_number = forms.CharField(label="차량 번호", max_length=15)

    class Meta:
        model = User
        fields = ("first_name","last_name","car_number","username", "password1", "password2", "email",)