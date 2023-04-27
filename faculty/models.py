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


class StudentInfo(models.Model):
    studentid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    studentmajor  = models.CharField(max_length = 100)
    studentyear = models.CharField(max_length = 100)
    gpa = models.DecimalField(max_digits = 2, decimal_places=1)

class Facultycomment(models.Model):
    facultyemail = models.CharField(max_length = 500)
    facultycomment = models.TextField()

class Award(models.Model):
    awardtype = models.CharField(max_length = 500)

class FacultyNomination(models.Model):
    facultyname = models.CharField(max_length = 100)
    awardtype = models.CharField(max_length = 100)

