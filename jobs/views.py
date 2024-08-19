from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    return render(request, 'jobs/homepage.html')

def login_page(request):
    return render(request, 'jobs/login.html')

def employer_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('employer_dashboard')  # Redirect to employer dashboard
        else:
            return render(request, 'jobs/employer_login.html', {'error': 'Invalid credentials'})
    return render(request, 'jobs/employer_login.html')

def job_seeker_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('job_seeker_dashboard')  # Redirect to job seeker dashboard
        else:
            return render(request, 'jobs/job_seeker_login.html', {'error': 'Invalid credentials'})
    return render(request, 'jobs/job_seeker_login.html')

def signup(request):
    return render(request, 'jobs/signup.html')

def employer_signup(request):
    if request.method == 'POST':
        company_name = request.POST['companyName']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = company_name
        user.save()
        return redirect('employer_login')  # Redirect to employer login page after successful signup
    return render(request, 'jobs/employer_signup.html')

def job_seeker_signup(request):
    if request.method == 'POST':
        full_name = request.POST['fullName']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = full_name
        user.save()
        return redirect('job_seeker_login')  # Redirect to job seeker login page after successful signup
    return render(request, 'jobs/job_seeker_signup.html')

@login_required
def job_seeker_dashboard(request):
    return render(request, 'jobs/job_seeker_dashboard.html')

@login_required
def employer_dashboard(request):
    return render(request, 'jobs/employer_dashboard.html')