from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class StudentCreationForm(UserCreationForm):
    
    class Meta:
        pass # Add fields here.

class StudentEditionForm(UserChangeForm):
    
    class Meta:
        pass # Add fields here.

