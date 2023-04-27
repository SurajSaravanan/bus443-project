from django.db import models

class StudentInfo(models.Model):
    studentid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    studentmajor  = models.CharField(max_length = 100)
    studentyear = models.CharField(max_length = 100)
    gpa = models.DecimalField(max_digits = 2, decimal_places=1)

class CourseInfo(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_title = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    course_section_code = models.CharField(max_length=10)
    course_department = models.CharField(max_length=100)
    instructor_full_name = models.CharField(max_length=100)

class StudentEnrollment(models.Model):
    enrollmentid = models.AutoField(primary_key=True)
    studentid = models.IntegerField()
    course_title = models.CharField(max_length=100, default='')





