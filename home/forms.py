import email
from pyexpat import model
import django
from django.forms import ModelForm, PasswordInput
from .models import Room
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RoomForm(ModelForm):
    class Meta:
        model=Room
        fields = '__all__' 
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    