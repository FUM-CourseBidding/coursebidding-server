from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Student

class StudentCreationForm(UserCreationForm):
    
    class Meta:
        model = Student
        fields = {'username',}

class StudentEditionForm(UserChangeForm):
    
    class Meta:
        model = Student
        fields = '__all__'
        

