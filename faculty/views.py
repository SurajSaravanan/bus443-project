from django.shortcuts import render
from django.http import HttpResponse
from faculty.models import StudentInfo, CourseInfo, StudentEnrollment
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Avg
# from faculty.forms import CommentForm


# Create your views here.
@login_required
def home(request):
    context = {'name':"Pradeep Patil"}
    return render(request,'faculty/home.html', context)
   
    
    
    #Data can be retrieved in 2 ways 
    #1) Using the Django query set 
    #2) Using raw SQL statements 
@login_required
def getstudentinfo(request):
    studentdata = StudentInfo.objects.all()
    paginator = Paginator(studentdata, 10)
    page = request.GET.get('page')
    pagedata = paginator.get_page(page)
    context = {'data':pagedata}
    return render(request,'faculty/studentinfo.html', context)

@login_required
def getcourseinfo(request):
    coursedata =CourseInfo.objects.all()
    paginator = Paginator(coursedata, 10)
    page = request.GET.get('page')
    pagedata = paginator.get_page(page)
    context = {'data':pagedata}
    return render(request,'faculty/courseinfo.html', context)

@login_required
def enrollmentinfo(request):
    studentdata = StudentInfo.objects.all()
    coursedata = CourseInfo.objects.all()
    enrollmentdata = StudentEnrollment.objects.all()
    context = {'student': studentdata, 'course':coursedata, 'enrollment': enrollmentdata}
    return render(request,'faculty/enrollment.html', context)

@login_required
def saveenrollment(request):
    if ('studentid' in request.GET and 'course_title' in request.GET):
        sid = request.GET.get('studentid')
        ctitle = request.GET.get('course_title')
        studentcount= StudentEnrollment.objects.filter(studentid=sid).count()
        recordcount= StudentEnrollment.objects.filter(studentid=sid, course_title = ctitle).count()
        if studentcount < 3 and recordcount == 0:
            data = StudentEnrollment(studentid=sid, course_title=ctitle)
            data.save()
            return HttpResponse('Success')
        return HttpResponse('Error')
    
    
#create a barchart to display number of nominations for each award type
def dashboard(request):
    enrolled_students = StudentEnrollment.objects.all().count()
    avg_gpa = StudentInfo.objects.all().aggregate(Avg('gpa'))['gpa__avg']
    avg_gpa = round(avg_gpa, 2)
    seniors = StudentInfo.objects.filter(studentyear='Senior').count()
    juniors = StudentInfo.objects.filter(studentyear='Junior').count()
    freshmen = StudentInfo.objects.filter(studentyear='Freshman').count()
    sophomore = StudentInfo.objects.filter(studentyear='Sophomore').count()
    num_courses = CourseInfo.objects.all().count()
    print("-----------------------")
    print(enrolled_students)
    print(avg_gpa)
    print(seniors)
    print(juniors)
    print(freshmen)
    print(sophomore)
    print(num_courses)

    context = {
        'num_students': enrolled_students,
        'avg_gpa': avg_gpa,
        'num_seniors': seniors,
        'num_juniors': juniors,
        'num_freshmen': freshmen,
        'num_sophomore': sophomore,
        'num_courses': num_courses,
    }

    return render(request, 'faculty/dashboard.html', context)






    



