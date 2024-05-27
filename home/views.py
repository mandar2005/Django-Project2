# home/views.py
from multiprocessing import context
from django.shortcuts import render , HttpResponse , get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AttendanceForm
from .models import Person , Attendance , Student
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import messages


from django import forms

def index(request):
    return render(request, 'home/index.html')

def private(request):
    return render(request, 'home/private.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'home/private.html')
        else:
            # Handle invalid login
            return  HttpResponse("Invalid Credential")

    return render(request, 'home/login.html')

#@login_required
"""
def attend(request):
	# dictionary for initial data with 
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["dataset"] = Person.objects.all()
		
	return render(request, "home/attend.html", context)
"""
def attend(request):
    dataset = Student.objects.all()
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['attendance_date']
            for person in dataset:
                status_field_name = 'status_' + str(person.id)
                status = form.cleaned_data[status_field_name]
                # Assuming you have a foreign key relationship between Attendance and Student
                Attendance.objects.create(student=person, date=date, status=status)
            return redirect('home:index')  # Redirect to a success page or wherever appropriate
    else:
        form = AttendanceForm()
    context = {'form': form, 'dataset': dataset}
    return render(request, 'home/attend.html', context)


@login_required
def about(request):
    return render(request, 'home/about.html')

@login_required
def attendance(request):
     
      # Get the logged-in student
    student = request.user.student

	# dictionary for initial data with 
	# field names as keys
    context ={}

	# add the dictionary during initialization
    context["dataset"] = Attendance.objects.filter(student=student)
		
    return render(request, "home/attendance.html", context)


def logout_view(request):
    logout(request)
    return render(request, 'home/login.html')

# views.py
 

def signin(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return render(request, 'home/index.html')  # Redirect to the home page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'home/signin.html', {'form': form})


"""
class AttendanceForm(forms.Form):
    def __init__(self, students, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        for student in students:
            self.fields[f"status_{student.id}"] = forms.ChoiceField(
                label=student.name,
                choices=(
                    ('Present', 'Present'),
                    ('Absent', 'Absent'),
                ),
                widget=forms.Select(attrs={'class': 'form-control'}),
            )

def attendance_form(request):
    if request.method == 'POST':
        students = User.objects.filter(groups__name='Students')
        form = AttendanceForm(students, request.POST)
        if form.is_valid():
            for student in students:
                status = form.cleaned_data[f"status_{student.id}"]
                # Process attendance data for each student
                Attendance.objects.create(student=student, status=status)
            return redirect('success-page')  # Replace 'success-page' with your actual URL name
    else:
        students = User.objects.filter(groups__name='Students')
        form = AttendanceForm(students)
    
    return render(request, 'attendance_form.html', {'form': form})

    """
# views.py
from django.shortcuts import render, redirect
from .forms import PersonForm

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/index.html')# Redirect to a success page
    else:
        form = PersonForm()
    return render(request, 'add_person.html', {'form': form})


def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            
            #students = Student.objects.all()
            form.save()
            return render(request, 'home/index.html')# Redirect to a success page
    else:
        form = AttendanceForm()
    students = Student.objects.all()    
    return render(request, 'home/mark.html', {'form': form})

"""
from django.shortcuts import render, redirect
from .forms import AttendanceForm
from .models import Student, Attendance
from django.contrib import messages

def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            students = Student.objects.all()
            for student in students:
                status = request.POST.get('status_' + str(student.id))
                Attendance.objects.create(student=student, date=date, status=status)
            messages.success(request, 'Attendance data added successfully!')
            return render(request, 'home/index.html')
    else:
        form = AttendanceForm()
        students = Student.objects.all()
    return render(request, 'home/mark.html', {'form': form, 'students': students})
    
"""


