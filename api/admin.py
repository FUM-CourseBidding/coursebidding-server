from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import StudentCreationForm, StudentEditionForm
from django.utils.translation import gettext_lazy as _

from .models import Student, Course

class Admin(UserAdmin):
    fieldsets = (
            (None, {'fields': ('username', 'password')}),
            (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
            (_('Permissions'), {
                'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            }),
            (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
            (_('Course binding'), {'fields': Student.course_bidding_fields}),
        )
    add_form = StudentCreationForm
    form = StudentEditionForm
    model = Student
    list_display = ['username', 'email',]

admin.site.register(Student, Admin)
admin.site.register(Course)