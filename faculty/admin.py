from django.contrib import admin
from faculty.models import FacultyInfo, StudentInfo, Award

# Register your models here.

admin.site.register(FacultyInfo)
admin.site.register(StudentInfo)
admin.site.register(Award)
