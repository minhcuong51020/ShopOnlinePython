from django.forms import ModelForm
from .models import User
class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'username', 'password']