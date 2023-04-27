from django.shortcuts import render
from django.http import HttpResponse
from faculty.models import FacultyInfo

# Create your views here.
def home(request):
    context = {'name':"Pradeep Patil"}
    return render(request,'faculty/home.html', context)
    #return HttpResponse('<h1>Home Page</h1>')
    
    
    #Data can be retrieved in 2 ways 
    #1) Using the Django query set 
    #2) Using raw SQL statements 
def getfacultyinfo(request):
    facultydata = FacultyInfo.objects.all()
    context = {'data':facultydata}
    return render(request,'faculty/facultyinfo.html', context)