from django.shortcuts import render
from django.http import HttpResponse
from faculty.models import FacultyInfo, Facultycomment, Award, FacultyNomination
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from faculty.forms import CommentForm


# Create your views here.
@login_required
def home(request):
    context = {'name':"Pradeep Patil"}
    return render(request,'faculty/home.html', context)
    #return HttpResponse('<h1>Home Page</h1>')
    
    
    #Data can be retrieved in 2 ways 
    #1) Using the Django query set 
    #2) Using raw SQL statements 
@login_required
def getfacultyinfo(request):
    facultydata = FacultyInfo.objects.all()
    paginator = Paginator(facultydata, 2)
    page = request.GET.get('page')
    pagedata = paginator.get_page(page)

    context = {'data':pagedata}
    return render(request,'faculty/facultyinfo.html', context)

#CSRF - Cross Site Request Forgery

# faculty comment page with faculty email and comment
def saveComment(request):
    if('useremail' in request.GET and 'usercomment' in request.GET):
        femail = request.GET.get('useremail')
        fcomment = request.GET.get('usercomment')
        
        data = Facultycomment(facultyemail = femail, facultycomment= fcomment)
        print(femail, fcomment)
        data.save()
        return HttpResponse('Success')
    

def commentpage(request):
    return render(request,'faculty/comment.html')


def commentformexample(request):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            form = CommentForm()
    context = {'form':form}
    return render(request,'faculty/commentform.html', context)

# faculty nomination page
def nominationinfo(request):
    facultydata = FacultyInfo.objects.all()
    awarddata = Award.objects.all()
    nominationdata = FacultyNomination.objects.all()
    context = {'faculty': facultydata, 'award':awarddata, 'nomination': nominationdata}
    return render(request,'faculty/nomination.html', context)

def savenomination(request):
    if ('facultyname' in request.GET and 'awardtype' in request.GET):
        fname = request.GET.get('facultyname')
        award = request.GET.get('awardtype')
        facultycount= FacultyNomination.objects.filter(facultyname=fname).count()
        if facultycount == 0:
            data = FacultyNomination(facultyname=fname, awardtype=award)
            data.save()
            return HttpResponse('Success')
        return HttpResponse('Error')
    
#create a barchart to display number of nominations for each award type
def chartdata(request):
    teachingcount = FacultyNomination.objects.filter(awardtype = 'Teaching').count()
    researchcount = FacultyNomination.objects.filter(awardtype = 'Research').count()
    outreachcount = FacultyNomination.objects.filter(awardtype = 'Outreach').count()
    context = {
        'teaching': teachingcount,
        'research': researchcount,
        'outreach': outreachcount
    }
    return render(request, 'faculty/chart.html', context)


