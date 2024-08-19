from django.urls import path
from .views import employer_dashboard, employer_signup, home, job_seeker_dashboard, job_seeker_signup, login_page, employer_login, job_seeker_login, signup

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('signup/employer/', employer_signup, name='employer_signup'),
    path('signup/job_seeker/', job_seeker_signup, name='job_seeker_signup'),
    path('login/', login_page, name='login'),
    path('login/employer/', employer_login, name='employer_login'),
    path('login/job_seeker/', job_seeker_login, name='job_seeker_login'),
    path('dashboard/job_seeker/', job_seeker_dashboard, name='job_seeker_dashboard'),
    path('dashboard/employer/', employer_dashboard, name='employer_dashboard'),
]