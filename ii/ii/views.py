from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import NameForm
from student.models import student
#def index(request):
  #  return HttpResponse("Hello, world. You're at the polls index.")




from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect

def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return render(request, 'ii/main.html')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'ii/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        #return HttpResponse("Hello,Login page")
        return render(request, 'ii/login.html')

def profile (request):
    return render(request,'ii/profile.html')


def single_student(request, institute_id):
    single_student = get_object_or_404(student, pk=institute_id)
    context = {"single_student": single_student}
    return render(request, "ii/profile.html", context)

def aboutus (request):
    return render(request,'ii/aboutus.html')

def home(request):
    return render(request,'ii/main.html')

def message(request):
    return render(request,'ii/message.html')



def thanks(request):
    return render(request,'ii/thanks.html')


def signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            b = student(first_name=form.cleaned_data["first_name"],last_name=form.cleaned_data["last_name"],gender=form.cleaned_data["gender"],citizen_id=form.cleaned_data["citizenid"],phone_number=form.cleaned_data["mobilenum"], address=form.cleaned_data["address"],age=form.cleaned_data["age"],email=form.cleaned_data["email"],class_name="")
            b.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'ii/signup.html', {'form': form})


def student_list(request):
    students = student.objects.all()
    #paginator = Paginator(students, 1)
    page = request.GET.get('page')
   # paged_students = paginator.get_page(page)

    context = {
        #"students": paged_students
        "students": students
    }
    return render(request, "ii/studentlist.html", context)




