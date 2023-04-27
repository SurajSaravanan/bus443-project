from django.db import models

# Create your models here.
# To make django create table execute python manage.py make migration python manage.py migrate
# adding data to a django model 
#1) Using the admin console - Recommended 
#2) Django shell - Recommended
#3) Using insert statement in pg Admin 

class FacultyInfo (models.Model):
    facultyid = models.IntegerField()
    facultyname = models.CharField(max_length = 100)
    facultyage = models.IntegerField()
    researcharea = models.TextField()