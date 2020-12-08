from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin

from .forms import StudentCreationForm, StudentEditionForm
from .models import Student

class Admin(UserAdmin):
    add_form = StudentCreationForm
    edit_form = StudentEditionForm
    model = Student
    list_display = ['email', 'username',]

admin.site.register(Student, Admin)