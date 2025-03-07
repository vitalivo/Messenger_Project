from django import forms
from .models import Room, User

class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['title']
        
class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'avatar']  # Убедитесь, что эти поля существуют в вашей модели User
