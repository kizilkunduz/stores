from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Profile, Store, Product
from django import forms 
from crispy_forms.helper import FormHelper


class CustomUserCreationForm(UserCreationForm):

    email= forms.EmailField()

    class Meta:

        model= User
        fields= UserCreationForm.Meta.fields + ('email',)


class StoreForm(forms.ModelForm):

    class Meta:

        model = Store
        fields= ['name', 'description']

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields= ['title', 'description', 'image']

    helper = FormHelper()