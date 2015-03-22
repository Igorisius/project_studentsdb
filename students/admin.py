from django.contrib import admin
from .models import Student
from .models import Group
from .models import Exam

admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Exam)
# Register your models here.
